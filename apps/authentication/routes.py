# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask import render_template, redirect, request, url_for
from flask_login import (
    current_user,
    login_user,
    logout_user
)
import sendgrid
from flask_dance.contrib.github import github
from apps import db, login_manager
from apps.authentication import blueprint
from apps.authentication.forms import LoginForm, CreateAccountForm
from apps.authentication.models import Users
import os
import json
from flask_mail import Message
from flask import current_app
from email.message import EmailMessage
import ssl
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from apps.authentication.util import verify_pass
from email.utils import formataddr


@blueprint.route('/')
def route_default():
    return redirect(url_for('authentication_blueprint.informationPage'))
# Login & Registration


@blueprint.route('/informationPage', methods=['GET', 'POST'])
def informationPage():
    if request.method == 'POST':
        name = request.form['name']
        email=request.form['email']
        try:
            email_sender = formataddr(('On Top Ads', 'ontopadsinc@gmail.com'))
            email_password = "dmyldtwkkwjtkoil"
            email_receiver=formataddr((name, email))
            subject = f"On Top Ads for {name}"

            em = MIMEMultipart('alternative')
            em['From'] = email_sender
            em['To'] = email_receiver
            em['Subject'] = subject
            text = f"Hello {name} and welcome to OTA!"
            html = ("""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"><html data-editor-version="2" class="sg-campaigns" xmlns="http://www.w3.org/1999/xhtml"> <head> <meta http-equiv="Content-Type" content="text/html; charset=utf-8"> <meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1"> <!--[if !mso]><!--> <meta http-equiv="X-UA-Compatible" content="IE=Edge"> <!--<![endif]--> <!--[if (gte mso 9)|(IE)]> <xml> <o:OfficeDocumentSettings> <o:AllowPNG/> 
            <o:PixelsPerInch>96</o:PixelsPerInch> </o:OfficeDocumentSettings> </xml> <![endif]--> <!--[if (gte mso 9)|(IE)]> <style type="text/css"> body {width: 600px;margin: 0 auto;} table {border-collapse: collapse;} table, td {mso-table-lspace: 0pt;mso-table-rspace: 0pt;} img {-ms-interpolation-mode: bicubic;} </style><![endif]--> <style type="text/css"> body, p, div { font-family: arial,helvetica,sans-serif; font-size: 14px; } body { color: #000000; } body a { color: #1188E6; text-decoration: none; } p { margin: 0; padding: 0; } table.wrapper { width:100% !important; table-layout: fixed; -webkit-font-smoothing: antialiased; -webkit-text-size-adjust: 100%; -moz-text-size-adjust: 100%; -ms-text-size-adjust: 100%; } 
            img.max-width { max-width: 100% !important; } .column.of-2 { width: 50%; } .column.of-3 { width: 33.333%; } .column.of-4 { width: 25%; } ul ul ul ul { list-style-type: disc !important; } ol ol { list-style-type: lower-roman !important; } ol ol ol { list-style-type: lower-latin !important; } ol ol ol ol { list-style-type: decimal !important; } @media screen and (max-width:480px) { .preheader .rightColumnContent, .footer .rightColumnContent { text-align: left !important; } .preheader .rightColumnContent div, .preheader .rightColumnContent span, .footer .rightColumnContent div, .footer .rightColumnContent span { text-align: left !important; } .preheader .rightColumnContent, .preheader .leftColumnContent { font-size: 80% !important; padding: 5px 0; } 
            table.wrapper-mobile { width: 100% !important; table-layout: fixed; } img.max-width { height: auto !important; max-width: 100% !important; } a.bulletproof-button { display: block !important; width: auto !important; font-size: 80%; padding-left: 0 !important; padding-right: 0 !important; } .columns { width: 100% !important; } .column { display: block !important; width: 100% !important; padding-left: 0 !important; padding-right: 0 !important; margin-left: 0 !important; margin-right: 0 !important; } .social-icon-column { display: inline-block !important; } } 
            </style> <style> @media screen and (max-width:480px) { table\0 { width: 480px !important; } } </style> <!--user entered Head Start--><!--End Head user entered--> </head> <body> <center class="wrapper" data-link-color="#1188E6" data-body-style="font-size:14px; font-family:arial,helvetica,sans-serif; color:#000000; background-color:#FFFFFF;"> <div class="webkit"> <table cellpadding="0" cellspacing="0" border="0" width="100%" class="wrapper" bgcolor="#FFFFFF"> <tr> <td valign="top" bgcolor="#FFFFFF" width="100%"> <table width="100%" role="content-container" class="outer" align="center" cellpadding="0" cellspacing="0" border="0"> <tr> <td width="100%"> <table width="100%" cellpadding="0" cellspacing="0" border="0"> <tr> <td> <!--[if mso]> <center> <table><tr><td width="600"> <![endif]--> <table width="100%" cellpadding="0" cellspacing="0" border="0" style="width:100%; max-width:600px;" align="center"> <tr> <td role="modules-container" style="padding:0px 0px 0px 0px; color:#000000; text-align:left;" bgcolor="#FFFFFF" width="100%" align="left"><table class="module preheader preheader-hide" role="module" data-type="preheader" border="0" cellpadding="0" cellspacing="0" width="100%" style="display: none !important; mso-hide: all; visibility: hidden; opacity: 0; color: transparent; height: 0; width: 0;"> <tr> <td role="module-content"> <p></p> </td> </tr> </table><table border="0" cellpadding="0" cellspacing="0" align="center" width="100%" role="module" data-type="columns" style="padding:1px 0px 7px 0px;" bgcolor="#FFFFFF" data-distribution="1,1"> 
            <tbody> <tr role="module-content"> <td height="100%" valign="top"><table width="300" style="width:300px; border-spacing:0; border-collapse:collapse; margin:0px 0px 0px 0px;" cellpadding="0" cellspacing="0" align="left" border="0" bgcolor="" class="column column-0"> <tbody> <tr> <td style="padding:0px;margin:0px;border-spacing:0;"><table class="wrapper" role="module" data-type="image" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="f83d9204-1606-4de1-a10e-3e92ac0f9fa5"> <tbody> <tr> <td style="font-size:6px; line-height:10px; padding:17px 44px 12px 0px;" valign="top" align="center"> <a href="http://ontopads.co"><img class="max-width" border="0" style="display:block; color:#000000; text-decoration:none; font-family:Helvetica, arial, sans-serif; font-size:16px; max-width:74% !important; width:74%; height:auto !important;" width="222" alt="" data-proportionally-constrained="true" data-responsive="true" src="http://cdn.mcauto-images-production.sendgrid.net/54bc28caa9b61446/ab764aca-41f3-45d8-8728-e2989a54a5d0/663x247.png"></a></td> </tr> </tbody> </table><table class="module" role="module" data-type="text" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="ffb4a968-f67f-4370-8c24-d00c8bdaaaff" data-mc-module-version="2019-10-22"> <tbody> <tr> <td style="padding:17px 0px 0px 30px; line-height:41px; text-align:inherit;" height="100%" valign="top" bgcolor="" role="module-content"><div><div style="font-family: inherit; text-align: left">
            <span style="font-family: arial, helvetica, sans-serif; font-size: 40px"><strong>PUT YOUR BUSINESS ON TOP WITH</strong></span></div><div style="font-family: inherit; text-align: left"><span style="font-family: arial, helvetica, sans-serif; font-size: 40px"><strong>ON TOP ADS</strong></span></div><div></div></div></td> </tr> </tbody> </table></td> </tr> </tbody> </table><table width="300" style="width:300px; border-spacing:0; border-collapse:collapse; margin:0px 0px 0px 0px;" cellpadding="0" cellspacing="0" align="left" border="0" bgcolor="" class="column column-1"> <tbody> <tr> <td style="padding:0px;margin:0px;border-spacing:0;"><table class="wrapper" role="module" data-type="image" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="310d916e-21da-4835-b221-8d57f8e2faed"> <tbody> <tr> <td style="font-size:6px; line-height:10px; padding:0px 0px 0px 0px;" valign="top" align="center"> <img class="max-width" border="0" style="display:block; color:#000000; text-decoration:none; font-family:Helvetica, arial, sans-serif; font-size:16px; max-width:100% !important; width:100%; height:auto !important;" width="300" alt="" data-proportionally-constrained="true" data-responsive="true" src="http://cdn.mcauto-images-production.sendgrid.net/54bc28caa9b61446/007a4a0d-35ab-448a-a0cf-a7dda428166e/612x339.jpg"> </td> </tr> </tbody> </table><table class="wrapper" role="module" data-type="image" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="863b51c8-0330-4f5b-9f02-53e548c007c5"> <tbody> <tr> <td style="font-size:6px; line-height:10px; padding:0px 0px 0px 0px;" valign="top" align="center"> 
            <img class="max-width" border="0" style="display:block; color:#000000; text-decoration:none; font-family:Helvetica, arial, sans-serif; font-size:16px; max-width:100% !important; width:100%; height:auto !important;" width="300" alt="" data-proportionally-constrained="true" data-responsive="true" src="http://cdn.mcauto-images-production.sendgrid.net/54bc28caa9b61446/fb14a0bd-4a3e-4540-af54-df1d0eb40f43/380x240.jpg"> </td> </tr> </tbody> </table></td> </tr> </tbody> </table></td> </tr> </tbody> </table><table border="0" cellpadding="0" cellspacing="0" align="center" width="100%" role="module" data-type="columns" style="padding:1px 1px 2px 0px;" bgcolor="" data-distribution="1"> <tbody> <tr role="module-content"> <td height="100%" valign="top"><table width="579" style="width:579px; border-spacing:0; border-collapse:collapse; margin:0px 10px 0px 10px;" cellpadding="0" cellspacing="0" align="left" border="0" bgcolor="" class="column column-0"> 
            <tbody> <tr> <td style="padding:0px;margin:0px;border-spacing:0;"><table class="module" role="module" data-type="text" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="faa687cb-ace6-491f-838f-036140a1f52f.2.1.1" data-mc-module-version="2019-10-22"> <tbody> <tr> <td style="padding:1px 0px 15px 20px; line-height:22px; text-align:inherit; background-color:#FFFFFF;" height="100%" valign="top" bgcolor="#FFFFFF" role="module-content"><div><div style="font-family: inherit; text-align: inherit"><br></div><div style="font-family: inherit; text-align: inherit">Hello """+ name+""",</div><div style="font-family: inherit; text-align: inherit"><br></div><div style="font-family: inherit; text-align: inherit">Thank you for signing up to receive updates about On Top Ads. We are thrilled to have you on board and are excited to share our progress with you.</div><div style="font-family: inherit; text-align: inherit"><br></div><div style="font-family: inherit; text-align: inherit">As you may know, we are currently in the MVP development stage for On Top Ads, working hard to create the ultimate solution for local businesses to advertise their products on multiple platforms at once. Our app will make it easy to schedule and customize posts, track and manage your advertising efforts, and reach a broader audience on popular platforms like Facebook, Craigslist, and Kijiji.</div><div style="font-family: inherit; text-align: inherit"><br></div><div style="font-family: inherit; text-align: inherit">We understand that staying up to date with the latest developments in the ecommerce industry is important for your business, which is why we will be sharing updates with you on our progress and new features as we work towards
             <strong>launching our trial stages in March.</strong></div><div style="font-family: inherit; text-align: inherit"><br></div><div style="font-family: inherit; text-align: inherit">In the meantime, we would like to invite you to take a look at our website and learn more about On Top Ads and the benefits it can provide for your business. If you have any questions or feedback, please don't hesitate to reach out to us at ontopadsinc@gmail.com.</div><div style="font-family: inherit; text-align: inherit"><br></div><div style="font-family: inherit; text-align: inherit">We appreciate your interest in On Top Ads and can't wait to share the full product with you soon.</div><div style="font-family: inherit; text-align: inherit"><br></div><div style="font-family: inherit; text-align: inherit">Best,</div><div style="font-family: inherit; text-align: inherit"><br>The On Top Ads Team</div><div></div></div></td> </tr> </tbody> </table><table border="0" cellpadding="0" cellspacing="0" class="module" data-role="module-button" data-type="button" role="module" style="table-layout:fixed;" width="100%" data-muid="74901292-bf55-4df1-8152-4d1ce4137f44.1.1"> <tbody> <tr> <td align="center" bgcolor="#ffffff" class="outer-td" style="padding:7px 4px 30px 20px; background-color:#ffffff;"> <table border="0" cellpadding="0" cellspacing="0" class="wrapper-mobile" style="text-align:center;"> <tbody> <tr> <td align="center" bgcolor="#22be59" class="inner-td" style="border-radius:6px; font-size:16px; text-align:center; background-color:inherit;"> <a href="ontopads.co" style="background-color:#22be59; border:0px solid #333333; border-color:#333333; border-radius:0px; border-width:0px; color:#ffffff; display:inline-block; font-size:12px; font-weight:normal; letter-spacing:0px; line-height:normal; padding:16px 30px 12px 30px; text-align:center; text-decoration:none; border-style:solid; font-family:helvetica,sans-serif;" target="_blank">LEARN MORE</a>
             </td> </tr> </tbody> </table> </td> </tr> </tbody> </table></td> </tr> </tbody> </table></td> </tr> </tbody> </table><table class="module" role="module" data-type="social" align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="4e616014-c5bd-4525-bcbf-2d9ef3084e48"> <tbody> <tr> <td valign="top" style="padding:20px 0px 20px 0px; font-size:6px; line-height:10px;" align="left"> <table align="left" style="-webkit-margin-start:auto;-webkit-margin-end:auto;"> <tbody><tr align="left"><td style="padding: 0px 5px;" class="social-icon-column"> <a role="social-icon-link" href="https://www.linkedin.com/company/on-top-ads/" target="_blank" alt="LinkedIn" title="LinkedIn" style="display:inline-block; background-color:#000000; height:25px; width:25px;"> <img role="social-icon" alt="LinkedIn" title="LinkedIn" src="https://mc.sendgrid.com/assets/social/white/linkedin.png" style="height:25px; width:25px;" height="25" width="25"> </a> </td></tr></tbody> </table> </td> </tr> </tbody> </table><div data-role="module-unsubscribe" class="module" role="module" data-type="unsubscribe" style="color:#000000; font-size:12px; line-height:20px; padding:0px 5px 16px 16px; text-align:right;" data-muid="4e838cf3-9892-4a6d-94d6-170e474d21e5.1"><div class="Unsubscribe--addressLine"><p class="Unsubscribe--senderName" style="font-family:georgia,serif; font-size:12px; line-height:20px;">Sven Jensen</p><p style="font-family:georgia,serif; font-size:12px; line-height:20px;"><a class="Unsubscribe--unsubscribeLink" href="{{{unsubscribe}}}" target="_blank" style="color:#717171;">Unsubscribe - to unsubscribe please reply to this email stating you wish to do so. Thanks!</a></p></div></td> </tr> 
             </table> <!--[if mso]> </td> </tr> </table> </center> <![endif]--> </td> </tr> </table> </td> </tr> </table> </td> </tr> </table> </div> </center> </body> </html>
            """)


            part1 = MIMEText(text, 'plain')
            part2 = MIMEText(html, 'html')

            em.attach(part1)
            em.attach(part2)
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smpt:
                smpt.login('ontopadsinc@gmail.com', email_password)
                smpt.sendmail(email_sender,email_receiver,em.as_string())

        except Exception as e:
            print(e)
            print('DIDNT WORK')
        

        # Open the JSON file in read mode
        with open('/Users/woodPecker/Desktop/software/OTA.v.0.3/OTA web app/apps/authentication/emails.json', 'r') as file:
            data = json.load(file)

        # Add the new name and email to the data
        data['name'] = name
        data['email'] = email

        # Open the JSON file in write mode
        with open('/Users/woodPecker/Desktop/software/OTA.v.0.3/OTA web app/apps/authentication/emails.json', 'w') as file:
            json.dump(data, file)


    return render_template('accounts/informationPage.html')


@blueprint.route('/team', methods=['GET'])
def team():
     return render_template('accounts/team.html')







@blueprint.route("/github")
def login_github():
    """ Github login """
    if not github.authorized:
        return redirect(url_for("github.login"))

    res = github.get("/user")
    return redirect(url_for('home_blueprint.index'))

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm(request.form)
    if 'login' in request.form:

        # read form data
        username = request.form['username']
        password = request.form['password']

        # Locate user
        user = Users.query.filter_by(username=username).first()

        # Check the password
        if user and verify_pass(password, user.password):

            login_user(user)
            return redirect(url_for('home_blueprint.dashboard'))

        # Something (user or pass) is not ok
        return render_template('accounts/login.html',
                               msg='Wrong user or password',
                               form=login_form)

    if not current_user.is_authenticated:
        return render_template('accounts/login.html',
                               form=login_form)
    return redirect(url_for('home_blueprint.dashboard'))









@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    create_account_form = CreateAccountForm(request.form)
    if 'register' in request.form:

        username = request.form['username']
        email = request.form['email']

        # Check usename exists
        user = Users.query.filter_by(username=username).first()
        if user:
            return render_template('accounts/register.html',
                                   msg='Username already registered',
                                   success=False,
                                   form=create_account_form)

        # Check email exists
        user = Users.query.filter_by(email=email).first()
        if user:
            return render_template('accounts/register.html',
                                   msg='Email already registered',
                                   success=False,
                                   form=create_account_form)

        # else we can create the user
        user = Users(**request.form)
        db.session.add(user)
        db.session.commit()

        # Delete user from session
        logout_user()
        
        return render_template('accounts/register.html',
                               msg='Account created successfully.',
                               success=True,
                               form=create_account_form)

    else:
        return render_template('accounts/register.html', form=create_account_form)


@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('authentication_blueprint.login'))


# Errors

@login_manager.unauthorized_handler
def unauthorized_handler():
    return render_template('home/page-403.html'), 403


@blueprint.errorhandler(403)
def access_forbidden(error):
    return render_template('home/page-403.html'), 403


@blueprint.errorhandler(404)
def not_found_error(error):
    return render_template('home/page-404.html'), 404


@blueprint.errorhandler(500)
def internal_error(error):
    return render_template('home/page-500.html'), 500
