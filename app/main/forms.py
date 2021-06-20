from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField
from wtforms.validators import Required,Email,EqualTo

class UpdateProfileForm(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Update')

class UploadBlogForm(FlaskForm):
    title = TextAreaField('Blog Title',validators=[Required()])
    blog =  TextAreaField('your blog',validators=[Required()])
    submit = SubmitField('Post')

class CommentsForm(FlaskForm):
    comment = TextAreaField('Type comment:',validators=[Required()])
    submit = SubmitField('Comment')
