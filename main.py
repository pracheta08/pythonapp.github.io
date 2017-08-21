#!usr/bin/python
import webapp2
from google.appengine.ext import ndb
   
   
html = """ 
           <html>
<head>
<title>INFORMATION</title>
</head>
  <body>
  <center>
  RESTAURANT FEEDBACK
    <form action = "/confirm" class="center" method = "post">
        FirstName:
        <input type = "text" name = "names" required/><br>
        LastName:
        <input type = "text" name = "lastname" required /><br>
        Address:
		<textarea name="address"  required></textarea>
        Phone number:
        <input type = "number" name="phone" required /><br>
        Gender:
      input type = "radio" name="gender" value = "Male" required/><br>
       input type = "radio" name="gender" value = "Female" required/><br>
        Feedback:
		<textarea name="feedback"  required></textarea>
      
        <input type = "submit" name = "submit" value = "SUBMIT">
        
        </form></center>
   </body>
</html> """  
   
   
class Product(ndb.Model):
     Fname = ndb.StringProperty(indexed=True)
     Lname = ndb.StringProperty(indexed=True)
     Address = ndb.TextProperty(indexed=True)
     Phone = ndb.IntegerProperty(indexed=True)
     Gender = ndb.StringProperty(indexed=True)
     Feedback = ndb.TextProperty(indexed=True)
     
     when = ndb.DateTimeProperty(auto_now_add=True)
	 
	 
	 
class MyHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(html)
		
		
		
		
class MainHandler(webapp2.RequestHandler):
   def post(self):
     Fname = self.request.get('names')
     Lname = self.request.get('lastname')
     Address = self.request.get('address')
     Phone =  int(self.request.get('phone'))
     Gender = self.request.get('gender')
     Feedback = self.request.get('feedback')
     restaurant = Product()
     restaurant.Fname=Fname
     restaurant.Lname=Lname
     restaurant.Address=Address
     restaurant.Phone=Phone
     restaurant.Gender=Gender
     restaurant.Feedback=Feedback
     restaurant.put()
     self.redirect('/')
	 
app = webapp2.WSGIApplication([('/', MyHandler),('/confirm', MainHandler)], 
 debug=True)
