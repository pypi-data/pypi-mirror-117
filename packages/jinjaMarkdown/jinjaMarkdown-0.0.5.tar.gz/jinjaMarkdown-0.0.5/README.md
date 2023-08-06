# Jinja2 Markdown Filter

This package offers a markdown filter to can be used to convert markdown to html code within a jinja2 template. 

# How to Use

1. First install the package

        pip install jinjaMarkdown

2. Import and Add the extension to your jinja enviroment (this should be done in app.py for flask)

        #import package
        from jinjaMarkdown.markdownExtension import markdownExtension
        
        #add markdownExtension to enviroment (by default jinja_env)
        app.jinja_env.add_extension(markdownExtension)

3. Use markdown filter as you would any other jinja filter
        
        {{ "# Hello World" | markdown }}

    The above code would be equivalent to
        
        "<p><h1>Hello World</h1></p>"

    If autoescape is on (as it is by default) this will not be rendered as html code and instead as a string.

4. Autoescape can be turned off like so:
        
        {% autoescape false %}
        {{ "# Hello World" | markdown }}
        {% endautoescape %}
      **Note:** Malicious code can be run while autoescape is turned off, so please keep your code secure.

# Markdown Syntax in Use

The markdown syntax used in this package follows [this guide](https://www.markdownguide.org/basic-syntax/). 

Only the best practices for markdown are implemented. If you are getting an error while using this package ensure you follow best practice first and that the syntax you are using is not included below.

## Basic Syntax Not Included (yet) 

   - Blockquotes
   - Lists
   - Code Blocks
   - Escaping Characters and Code
   - Reference links
   - Links using angular brackets 




