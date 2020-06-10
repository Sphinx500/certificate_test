from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.config import Configurator
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
authn_policy = AuthTktAuthenticationPolicy('seekrit', hashalg='sha512')
authz_policy = ACLAuthorizationPolicy()
config = Configurator()
config.set_authentication_policy(authn_policy)
config.set_authorization_policy(authz_policy)

def hello_world(request):
    return Response('Hello pyramid certificate!')


if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()