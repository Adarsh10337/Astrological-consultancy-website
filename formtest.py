import cgi
print("Content-type: text/html\r\n\r\n") 
print("<html><body>") 
print("<h1> Hello Program! </h1>") 
# Using the inbuilt methods
# Create instance of FieldStorage 
form = cgi.FieldStorage() 
# Get data from fields
if form.getvalue("first_name"):
    first_name = form.getvalue('first_name')
    last_name  = form.getvalue('last_name')
    print("<h2>Hello %s %s</h2>" % (first_name, last_name))
print("</body></html>")