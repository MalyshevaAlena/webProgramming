from views import BlogRead, BlogIndex, BlogCreate, BlogDelete, BlogUpdate
from wsgi_basic_auth import BasicAuth

# third-party
import selector


def make_wsgi_app():
    adm_group = {
        'admin': '1',
        'admin2': '2'
    }
    md_group = {
        'moderator': '1',
        'moderator2': '2'
    }
    users_group = {
        'user': '1',
        'user2': '2'
    }

    moder_admin = adm_group.update(md_group)
    moder_user = md_group.update(users_group)

    # BasicAuth applications
    create = BasicAuth(BlogCreate, 'www', moder_admin)
    update = BasicAuth(BlogUpdate, 'www', md_group)
    delete = BasicAuth(BlogDelete, 'www', moder_user)

    # URL dispatching middleware
    dispatch = selector.Selector()
    dispatch.add('/', GET=BlogIndex)
    dispatch.prefix = '/article'
    dispatch.add('/add', GET=create, POST=create)
    dispatch.add('/{id:digits}', GET=BlogRead)
    dispatch.add('/{id:digits}/edit', GET=update, POST=update)
    dispatch.add('/{id:digits}/delete', GET=delete)

    return dispatch

if __name__ == '__main__':

    app = make_wsgi_app()

    from whitenoise import WhiteNoise
    app = WhiteNoise(app)
    app.add_files('./static/', prefix='static/')

    from paste.httpserver import serve
    serve(app, host='0.0.0.0', port=8000)
