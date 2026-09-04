# GreaterHeight Technologies — Static Website Rebuild v12

Production-oriented static rebuild of the captured GreaterHeight Technologies website using HTML, CSS and JavaScript, with DNN/WebForms runtime removed.

## Deploy
1. Upload the contents of this folder to the web document root.
2. Keep the existing relative directory structure intact.
3. On Apache use `.htaccess`; on IIS use `web.config`; on compatible static hosts use `_headers`.
4. Test `/index.html`, `/Where-We-Are.html`, a nested page, CSS, JavaScript and document links.

## Contact form
The contact form does not claim server-side submission. It validates the fields and opens the visitor's configured email application with a pre-filled message addressed to `sales@greaterheight.tech`.

## QA limitation
Automated structural and link QA has been completed. Browser screenshot rendering was blocked by the execution environment, so final visual acceptance should be performed on staging before DNS cutover.
