## Summary

We cover webscraping static website using `requests` and `BeautifulSoup`.

### Dynamic Sites

If you try to donwload the HTML of a site but notice the page source is not what is being displayed by your browser, you've likely encountered a dynamic site.  Dynamic sites will send JavaScript code to the clients' browser, which then is used to create the HTML.  If you want to scrape a dynamic website, you will need something that will render the JavaScript, similiar to how your browser does.   I have successfully scraped dyanmic sites using selenium--which basically allows you to control your webbrowser (like FireFox or Chrome) using Python.  I have also recently read about requests-html, but haven't tried it.

* [selenium](https://selenium-python.readthedocs.io)
* [requests-html](https://github.com/psf/requests-html)
