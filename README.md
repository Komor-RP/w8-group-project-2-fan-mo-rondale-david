# QuestionBox

## Requirements

* Users can view questions and answers
* Registered users can ask questions
* Registered users can add answers to any question
* The question's creator can mark answers as correct
* Registered users can "star" questions and answers they like

### How questions and answers work

Questions have a title and a body. Allow your users to use [Markdown](https://en.wikipedia.org/wiki/Markdown) for authoring question bodies. [Python-Markdown](https://python-markdown.github.io/) can turn Markdown into HTML for you. You will also want to prevent people from putting unauthorized HTML into your Markdown code. [mdx-bleach](https://github.com/Wenzil/mdx_bleach) is a Python-Markdown extension that looks like it will work. Questions cannot be edited once they have been asked. A question can be deleted by its author. If it is deleted, all associated answers should also be deleted.

Answers just have a body and are connected to a question. Answers can also use Markdown.

Every question and every answer should be associated with a user.  A user should be able to view all their questions on a user profile page.

When a user answers a question, the question's author should receive an email with a link to the answer.

### How much of this is API + JavaScript?

Adding answers should happen in the page with no page load, thereby needing Ajax. Likewise, "starring" questions and answers and marking answers as correct should happen via Ajax.

The rest of the application can be plain old Django views, although you can use JavaScript + an API to load questions and answers if you want.
