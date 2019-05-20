from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class CheckForm(FlaskForm):
    sex = StringField('Пол', validators=[DataRequired()])
    cp = StringField('Тип боли в груди(1-4)', validators=[DataRequired()])
    rbp = StringField('Кровяное давление в покое', validators=[DataRequired()])
    sc = StringField('Уровень холерестина в мг / дл', validators=[DataRequired()])
    fbs = StringField('Уровень сахара в крови(натощак)', validators=[DataRequired()])
    rer = StringField('Лектрокардиографические результаты покоя', validators=[DataRequired()])
    mhra = StringField('Максимальная частота пульса', validators=[DataRequired()])
    eia = StringField('Cтенокардия, вызванная физической нагрузкой', validators=[DataRequired()])
    oldpeak = StringField('Депрессия ST, вызванная физическими упражнениями относительно отдыха', validators=[DataRequired()])
    slope = StringField('Наклон пика упражнений сегмента ST', validators=[DataRequired()])
    nmv = StringField('Количество крупных сосудов (0-3), окрашенных с помощью флюороскопии', validators=[DataRequired()])
    tal = StringField('Тал: 3 = нормальный; 6 = исправленный дефект; 7 = обратимый дефект', validators=[DataRequired()])
    #trestbps = StringField('trestbps', validators=[DataRequired()])
    #chol = StringField('chol', validators=[DataRequired()])
    submit = SubmitField('Отправить')


