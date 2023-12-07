<!DOCTYPE html>
<html lang="en">
<body>

<h1>Project Title</h1>

<h2>To-Do List GUI in Python</h2>

<p>A simple and user-friendly To-Do List application with a graphical user interface (GUI) built using Python and Tkinter.</p>

<h2>Table of Contents</h2>

<ul>
    <li><a href="#features">Features</a></li>
    <li><a href="#how-it-works">How It Works</a></li>
    <li><a href="#screenshots">Screenshots</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#dependencies">Dependencies</a></li>
    <li><a href="#how-to-contribute">How to Contribute</a></li>
   
</ul>

<h2>Features</h2>

<ul>
    <li><strong>Add Tasks:</strong> Easily add new tasks to your to-do list.</li>
    <li><strong>Delete Tasks:</strong> Remove completed tasks with a single click.</li>
    <li><strong>Persistent Storage:</strong> Tasks are saved to a text file, ensuring your to-do list persists between sessions.</li>
</ul>

<h2>How It Works</h2>

<ol>
    <li><strong>Adding Tasks:</strong>
        <ul>
            <li>Type your task in the input field.</li>
            <li>Click the "ADD" button to add the task to the list.</li>
        </ul>
    </li>
    <li><strong>Deleting Tasks:</strong>
        <ul>
            <li>Click the delete icon next to a task to remove it from the list.</li>
        </ul>
    </li>
    <li><strong>Persistence:</strong>
        <ul>
            <li>Tasks are saved to a text file (<code>todos.txt</code>).</li>
            <li>The application loads existing tasks from the file on startup.</li>
            <li>Changes are saved automatically, ensuring your to-do list is preserved.</li>
        </ul>
    </li>
</ol>

<h2>Screenshots</h2>

<img src="imgs/todoApp.png" alt="To-Do List Screenshot">

<h2>Getting Started</h2>

<h3>Prerequisites</h3>

<ul>
    <li>Python 3.x</li>
</ul>

<h3>Installation</h3>

<ol>
    <li>Clone the repository:</li>
</ol>

<pre><code>git clone https://github.com/vardhan-ganugula/python_gui_todos.git
</code></pre>

<ol start="2">
    <li>Run the application:</li>
</ol>

<pre><code>python todo.py
</code></pre>

<h2>Dependencies</h2>

<ul>
    <li><a href="https://docs.python.org/3/library/tkinter.html">Tkinter</a></li>
    <li><a href="https://pillow.readthedocs.io/en/stable/">Pillow (PIL)</a></li>
</ul>

<h2>How to Contribute</h2>

<p>If you'd like to contribute, please follow these steps:</p>

<ol>
    <li>Fork the repository.</li>
    <li>Create a new branch: <code>git checkout -b feature/your-feature-name</code></li>
    <li>Make your changes and commit them: <code>git commit -m 'Add some feature'</code></li>
    <li>Push to the branch: <code>git push origin feature/your-feature-name</code></li>
    <li>Submit a pull request.</li>
</ol>


</body>
</html>
