# Dp-189 TAQC Opencart automation

<p>The main goals of this repository is to provide automated test suite  for
<a href="http://34.71.14.206/">OpenCart</a> e-commerce platform.</p>

# Project structure

<p>The following directories tree outlines the most important information about project structure:</p>
<pre lang="text"><code>.
├── README.md                 &lt;= This file which documents the project.
├── dp189                     &lt;= a root directory
│   ├── driver                &lt;= WebDriver for automated testing         
│   ├── pages                 &lt;= Page-Object representation of online-store
│   ├── tests                 &lt;= Automated tests for selected pages
│   ├── testsData             &lt;= Test data for parameterized tests
│   │   ├── checkout_page 
│   │   ├── product_page
│   │   ├── register_page
│   │   └── shopping_cart
│   ├── components.py         &lt;= Component of the web-page that helps perform a specific task
│   ├── constants.py          &lt;= Static strings that used as arguments by executing automated tests
│   ├── locators.py           &lt;= References to a corresponding element on the actual web page
│   └── routes.py             &lt;= Constructor of links to online-store web-pages
└── requirements.txt          &lt;= Python packages for automated tests execution
</code></pre>

<h2>Usage of automated tests</h2>
<p>Please use Python version <code>3.6</code> or greater for the test execution.</p>
<p>Before running any command, please install required Python's dependencies with</p>
<div><pre>pip install -r requirements.txt</pre></div>

<h3>Code assessment</h3>
<p>To check correctness of the code the following tools were used:</p>
<li><a href="https://pylint.org" rel="nofollow">Pylint</a> analyzes the code and assesses it accordingly.</li>
<li><a href="http://flake8.pycqa.org/en/latest/" rel="nofollow">flake8</a> applies some style checks on the code.</li>
<li><a href="http://www.pydocstyle.org/en/stable/" rel="nofollow">pydocstyle</a> analyses the quality of docstrings.</li>