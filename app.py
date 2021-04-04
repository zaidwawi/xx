#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from flask import (
    Flask,
    request,
    abort,
    jsonify
    )
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Actor, Movie, rollback
from auth import requires_auth, AuthError


def create_app(test_config=None):

    # create and configure the app

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors(jwk):
        return (jsonify({'success': True, 'actors': [actor.format()
                for actor in Actor.query.all()]}), 200)

    @app.route('/actors/<int:actor_id>', methods=['GET'])
    @requires_auth('get:actors')
    def get_actor(jwk, actor_id):
        actor = Actor.query.get(actor_id)
        if actor is None:
            abort(404)
        return (jsonify({'success': True, 'actor': actor.format()}),
                200)

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def post_actors(jwk):
        body = request.get_json()
        new_actor = Actor()

        name = body.get('name')
        age = body.get('age')
        gender = body.get('gender')

        if name is None or age is None or gender is None:
            abort(400)
        try:

            new_actor.name = name
            new_actor.age = age
            new_actor.gender = gender

            new_actor.insert()
        except Exception:
            abort(500)

        return (jsonify({'success': True,
                'created_actor': new_actor.format()}), 200)

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def edit_actors(jwk, actor_id):
        body = request.get_json()
        actor = Actor.query.get(actor_id)
        name = (body.get('name') if body.get('name') else actor.name)
        age = (body.get('age') if body.get('age') else actor.age)
        gender = (
            body.get('gender') if body.get('gender')
            else actor.gender
            )

        if actor is None:
            abort(404)

        try:
            actor.name = name
            actor.age = age
            actor.gender = gender

            actor.update()
        except Exception:
            rollback()
            abort(500)

        return (jsonify({'success': True,
                'patched_actor': actor.format()}), 200)

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actors(jwk, actor_id):
        actor = Actor.query.get(actor_id)
        if actor is None:
            abort(404)

        try:
            actor.delete()
        except Exception:
            rollback()
            abort(500)

        return (jsonify({'success': True,
                'deleted_actor': actor.format()}), 200)

    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies(jwk):
        return jsonify({'success': True, 'movies': [movie.format()
                       for movie in Movie.query.all()]})

    @app.route('/movies/<int:movie_id>', methods=['GET'])
    @requires_auth('get:movies')
    def get_movie(jwk, movie_id):
        movie = Movie.query.get(movie_id)
        if movie is None:
            abort(404)
        return (jsonify({'success': True, 'movie': movie.format()}),
                200)

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def post_movies(jwk):
        body = request.get_json()

        title = body.get('title')
        release_date = body.get('release_date')

        if title is None or release_date is None:
            abort(400)

        try:
            new_movie = Movie()
            new_movie.title = title
            new_movie.release_date = release_date

            new_movie.insert()
        except Exception:
            abort(500)

        return (jsonify({'success': True,
                'created_movie': new_movie.format()}), 200)

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def edit_movies(jwk, movie_id):
        body = request.get_json()
        movie = Movie.query.get(movie_id)

        if movie is None:
            abort(404)

        title = (
            body.get('title') if body.get('title')
            else movie.title
            )
        release_date = (
            body.get('relaese_date') if body.get('release_date')
            else movie.relaese_date
            )

        try:
            movie.title = title
            movie.relaese_date = release_date

            movie.update()
        except Exception:
            abort(500)

        return (jsonify({'success': True,
                'patched_movie': movie.format()}), 200)

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movies(jwk, movie_id):
        movie = Movie.query.get(movie_id)
        if movie is None:
            abort(404)

        try:
            movie.delete()
        except Exception:
            rollback()
            abort(500)

        return (jsonify({'success': True,
                'deleted_movie': movie.format()}), 200)

    @app.errorhandler(400)
    def bad_request(error):
        return (jsonify({'success': False, 'error': 400,
                'message': 'Bad request'}), 400)

    @app.errorhandler(404)
    def resource_not_found_error(error):
        return (jsonify({'success': False, 'error': 404,
                'message': 'Resource not found'}), 404)

    @app.errorhandler(422)
    def unprocessable(error):
        return (jsonify({'success': False, 'error': 422,
                'message': 'unprocessable'}), 422)

    @app.errorhandler(401)
    def unauthorized(error):
        return (jsonify({'success': False, 'error': 401,
                'message': 'Unauthorized'}), 401)

    @app.errorhandler(403)
    def forbidden(error):
        return (jsonify({'success': False, 'error': 403,
                'message': 'Forbidden'}), 403)

    @app.errorhandler(500)
    def internal_server_error(error):
        return (jsonify({'success': False, 'error': 500,
                'message': 'Internal server error'}), 500)

    @app.errorhandler(AuthError)
    def authentication_error(error):
        return (jsonify({'success': False, 'error': error.status_code,
                'message': error.error}), error.status_code)

    return app


APP = create_app()

if __name__ == '__main__':
    APP.run()
