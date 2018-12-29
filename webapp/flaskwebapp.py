import copy
from decimal import *
from flask_wtf import FlaskForm
from flask import Flask, render_template, flash, request,url_for,redirect
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length
import sys
sys.path.append("..")
import scrape_views


# App config.
app = Flask(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

 
class Rose(FlaskForm):
    name = TextField('Name:', validators=[DataRequired()])
    #wiki=BooleanField('Display only wikipedia US TV viewers')
    #imdb=BooleanField('Display only imdb ratings')
    bar=BooleanField('Display bar chart')
    avg=BooleanField('Display averaged chart')
 
@app.route("/", methods=['GET', 'POST'])
def home():
    form = Rose()
   
    if request.method == 'POST':
 
       if form.validate:
        #Access data in the form
        
        show=(request.form.get('name'))
         #request.form.get returns true if the toggle switch is pushed to imdb      
        if request.form.get('toggleswitch'):
           b="y"
           #setting wiki false
           a="None"
		  
        else :
		   #setting imdb false
           b="None"
           a="y"
        if request.form.get('bar')=="y":
           c="y"
        else :
           c="None"
        
        if request.form.get('avg')=="y":
           d="y"
        else :
            d="None"
        
                

        
        
        return redirect(url_for('tv_series',show=show,a=a,b=b,c=c,d=d))
  
  
    return render_template("home.html",form = form)

@app.route("/tvseries/<show>/<a>/<b>/<c>/<d>",methods=['GET','POST'])
def tv_series(show,a,b,c,d):
     
    if b=="y":
        rang=[]
        img_file=0
        image_file=0
        imdburl = scrape_views.get_link(show, ' imdb', 'https://www.imdb.com')
        wikiurl = scrape_views.get_link(show, ' episodes wikipedia','https://en.wikipedia.org')
        k=scrape_views.get_seasons_imdb(imdburl)
        views, average = scrape_views.imdbscrape(imdburl,2)
        for item in average:
            rang.append(item[0])                
        ["%.2f" % e for e in rang]
        [Decimal("%.2f" % e) for e in rang]# to round off the numbers in the list
        data = [float(Decimal("%.2f" % e)) for e in rang]       
        if c=="y":
            scrape_views.barchart(copy.deepcopy(views),show,1)
            image_file=url_for('static',filename=show+'barchart.png')
                   
        if d=="y":
            scrape_views.average_plot(views, average,show,1)
            img_file=url_for('static',filename=show+'avgchart.png')
           
           
            
   
    return render_template("tvseries.html",show=show,imdburl=imdburl,k=k,views=views,data=data,c=c,d=d,image_file=image_file,img_file=img_file)

 
if __name__ == "__main__":
    app.run(debug=True) 