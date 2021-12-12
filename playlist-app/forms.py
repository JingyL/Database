"""Forms for playlist app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, SelectField,TextAreaField

from wtforms.validators import InputRequired, Optional, URL


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    # Add the necessary code to use this form
    name = StringField("name", validators=[
                       InputRequired(message="Name can't be blank")])
    description = TextAreaField("description", validators=[
                       InputRequired(message="Description can't be blank")])
 



class SongForm(FlaskForm):
    """Form for adding songs."""

    # Add the necessary code to use this form
    title = StringField("title", validators=[
                       InputRequired(message="Title can't be blank")])
    artist = StringField("artist", validators=[
                       InputRequired(message="Artist can't be blank")])


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
