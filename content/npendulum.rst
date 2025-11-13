====================
Dynamics with Python
====================

:subtitle: balancing the five link pendulum
:description: A post on using the PyDy workflow to control the n-link pendulum.
:date: 2013-01-27 16:46:00
:slug: npendulum
:tags: python, pydy, dynamics, control, animation

.. raw:: html

   <style type="text/css">
   /**
    * HTML5 ✰ Boilerplate
    *
    * style.css contains a reset, font normalization and some base styles.
    *
    * Credit is left where credit is due.
    * Much inspiration was taken from these projects:
    * - yui.yahooapis.com/2.8.1/build/base/base.css
    * - camendesign.com/design/
    * - praegnanz.de/weblog/htmlcssjs-kickstart
    */
   
   
   /**
    * html5doctor.com Reset Stylesheet (Eric Meyer's Reset Reloaded + HTML5 baseline)
    * v1.6.1 2010-09-17 | Authors: Eric Meyer & Richard Clark
    * html5doctor.com/html-5-reset-stylesheet/
    */
   
   pre.ipynb {
     color: black;
     background: #f7f7f7;
     border: 0;
     box-shadow: none;
     margin-bottom: 0;
     padding: 0;
   }
   
   h1.ipynb h2.ipynb h3.ipynb h4.ipynb h5.ipynb h6.ipynb {h1.ipynb h2.ipynb ... {
   margin: 0;
   padding: 0;
   border: 0;
   font-size: 100%;
   font: inherit;
   vertical-align: baseline;i
   }
   
   /*html, body,*/ div, span, object, iframe,
   /*h1, h2, h3, h4, h5, h6,*/ p, blockquote, pre,
   abbr, address, cite, code, del, dfn, em, img, ins, kbd, q, samp,
   small, strong, sub, sup, var, b, i, dl, dt, dd, ol, ul, li,
   fieldset, form, label, legend,
   table, caption, tbody, tfoot, thead, tr, th, td,
   article, aside, canvas, details, figcaption, figure,
   footer, header, hgroup, menu, nav, section, summary,
   time, mark, audio, video {
     margin: 0;
     padding: 0;
     border: 0;
     font-size: 100%;
     font: inherit;
     vertical-align: baseline;
   }
   
   sup { vertical-align: super; }
   sub { vertical-align: sub; }
   
   article, aside, details, figcaption, figure,
   footer, header, hgroup, menu, nav, section {
     display: block;
   }
   
   blockquote, q { quotes: none; }
   
   blockquote:before, blockquote:after,
   q:before, q:after { content: ""; content: none; }
   
   ins { background-color: #ff9; color: #000; text-decoration: none; }
   
   mark { background-color: #ff9; color: #000; font-style: italic; font-weight: bold; }
   
   del { text-decoration: line-through; }
   
   abbr[title], dfn[title] { border-bottom: 1px dotted; cursor: help; }
   
   table { border-collapse: collapse; border-spacing: 0; }
   
   hr { display: block; height: 1px; border: 0; border-top: 1px solid #ccc; margin: 1em 0; padding: 0; }
   
   input, select { vertical-align: middle; }
   
   
   /**
    * Font normalization inspired by YUI Library's fonts.css: developer.yahoo.com/yui/
    */
   
   div.ipynb { font:13px/1.231 sans-serif; *font-size:small; } /* Hack retained to preserve specificity */
   select, input, textarea, button { font:99% sans-serif; }
   
   /* Normalize monospace sizing:
      en.wikipedia.org/wiki/MediaWiki_talk:Common.css/Archive_11#Teletype_style_fix_for_Chrome */
   pre, code, kbd, samp { font-family: monospace, sans-serif; }
   
   em,i { font-style: italic; }
   b,strong { font-weight: bold; }
   
   </style>
   <style type="text/css">
   
   /* Flexible box model classes */
   /* Taken from Alex Russell http://infrequently.org/2009/08/css-3-progress/ */
    
   .hbox {
   	display: -webkit-box;
   	-webkit-box-orient: horizontal;
   	-webkit-box-align: stretch;
    
   	display: -moz-box;
   	-moz-box-orient: horizontal;
   	-moz-box-align: stretch;
    
   	display: box;
   	box-orient: horizontal;
   	box-align: stretch;
   }
    
   .hbox > * {
   	-webkit-box-flex: 0;
   	-moz-box-flex: 0;
   	box-flex: 0;
   }
    
   .vbox {
   	display: -webkit-box;
   	-webkit-box-orient: vertical;
   	-webkit-box-align: stretch;
    
   	display: -moz-box;
   	-moz-box-orient: vertical;
   	-moz-box-align: stretch;
    
   	display: box;
   	box-orient: vertical;
   	box-align: stretch;
   }
    
   .vbox > * {
   	-webkit-box-flex: 0;
   	-moz-box-flex: 0;
   	box-flex: 0;
   }
     
   .reverse {
   	-webkit-box-direction: reverse;
   	-moz-box-direction: reverse;
   	box-direction: reverse;
   }
    
   .box-flex0 {
   	-webkit-box-flex: 0;
   	-moz-box-flex: 0;
   	box-flex: 0;
   }
    
   .box-flex1, .box-flex {
   	-webkit-box-flex: 1;
   	-moz-box-flex: 1;
   	box-flex: 1;
   }
    
   .box-flex2 {
   	-webkit-box-flex: 2;
   	-moz-box-flex: 2;
   	box-flex: 2;
   }
    
   .box-group1 {
   	-webkit-box-flex-group: 1;
   	-moz-box-flex-group: 1;
   	box-flex-group: 1;
   }
    
   .box-group2 {
   	-webkit-box-flex-group: 2;
   	-moz-box-flex-group: 2;
   	box-flex-group: 2;
   }
    
   .start {
   	-webkit-box-pack: start;
   	-moz-box-pack: start;
   	box-pack: start;
   }
    
   .end {
   	-webkit-box-pack: end;
   	-moz-box-pack: end;
   	box-pack: end;
   }
    
   .center {
   	-webkit-box-pack: center;
   	-moz-box-pack: center;
   	box-pack: center;
   }
   
   </style>
   <style type="text/css">
   /**
    * Primary styles
    *
    * Author: IPython Development Team
    */
   
   
   div.ipynb {
       overflow: hidden;
   }
   
   span#save_widget {
       padding: 5px;
       margin: 0px 0px 0px 300px;
       display:inline-block;
   }
   
   span#notebook_name {
       height: 1em;
       line-height: 1em;
       padding: 3px;
       border: none;
       font-size: 146.5%;
   }
   
   .ui-menubar-item .ui-button .ui-button-text {
       padding: 0.4em 1.0em;
       font-size: 100%;
   }
   
   .ui-menu {
     -moz-box-shadow:    0px 6px 10px -1px #adadad;
     -webkit-box-shadow: 0px 6px 10px -1px #adadad;
     box-shadow:         0px 6px 10px -1px #adadad;
   }
   
   .ui-menu .ui-menu-item a {
       border: 1px solid transparent;
       padding: 2px 1.6em;
   }
   
   .ui-menu .ui-menu-item a.ui-state-focus {
       margin: 0;
   }
   
   .ui-menu hr {
       margin: 0.3em 0;
   }
   
   #menubar_container {
       position: relative;
   }
   
   #notification {
       position: absolute;
       right: 3px;
       top: 3px;
       height: 25px;
       padding: 3px 6px;
       z-index: 10;
   }
   
   #toolbar {
       padding: 3px 15px;
   }
   
   #cell_type {
       font-size: 85%;
   }
   
   
   div#main_app {
       width: 100%;
       position: relative;
   }
   
   span#quick_help_area {
       position: static;
       padding: 5px 0px;
       margin: 0px 0px 0px 0px;
   }
   
   .help_string {
       float: right;
       width: 170px;
       padding: 0px 5px;
       text-align: left;
       font-size: 85%;
   }
   
   .help_string_label {
       float: right;
       font-size: 85%;
   }
   
   div#notebook_panel {
       margin: 0px 0px 0px 0px;
       padding: 0px;
   }
   
   div#notebook {
       overflow-y: scroll;
       overflow-x: auto;
       width: 100%;
       /* This spaces the cell away from the edge of the notebook area */
       padding: 5px 5px 15px 5px;
       margin: 0px;
       background-color: white;
   }
   
   div#pager_splitter {
       height: 8px;
   }
   
   div#pager {
       padding: 15px;
       overflow: auto;
       display: none;
   }
   
   div.ui-widget-content {
       border: 1px solid #aaa;
       outline: none;
   }
   
   .cell {
       border: 1px solid transparent;
   }
   
   div.cell {
       width: 100%;
       padding: 5px 5px 5px 0px;
       /* This acts as a spacer between cells, that is outside the border */
       margin: 2px 0px 2px 0px;
   }
   
   div.code_cell {
       background-color: white;
   }
   
   /* any special styling for code cells that are currently running goes here */
   div.code_cell.running {
   }
   
   div.prompt {
       /* This needs to be wide enough for 3 digit prompt numbers: In[100]: */
       width: 11ex;
       /* This 0.4em is tuned to match the padding on the CodeMirror editor. */
       padding: 0.4em;
       margin: 0px;
       font-family: monospace;
       text-align:right;
   }
   
   div.input {
       page-break-inside: avoid;
   }
   
   /* input_area and input_prompt must match in top border and margin for alignment */
   div.input_area {
       color: black;
       border: 1px solid #ddd;
       border-radius: 3px;
       background: #f7f7f7;
   }
   
   div.input_prompt {
       color: navy;
       border-top: 1px solid transparent;
   }
   
   div.output_wrapper {
       /* This is a spacer between the input and output of each cell */
       margin-top: 5px;
       margin-left: 5px;
       /* FF needs explicit width to stretch */
       width: 100%;
       /* this position must be relative to enable descendents to be absolute within it */
       position: relative;
   }
   
   /* class for the output area when it should be height-limited */
   div.output_scroll {
     /* ideally, this would be max-height, but FF barfs all over that */
     height: 24em;
     /* FF needs this *and the wrapper* to specify full width, or it will shrinkwrap */
     width: 100%;
     
     overflow: auto;
     border-radius: 3px;
     box-shadow: inset 0 2px 8px rgba(0, 0, 0, .8);
   }
   
   /* output div while it is collapsed */
   div.output_collapsed {
     margin-right: 5px;
   }
   
   div.out_prompt_overlay {
     height: 100%;
     padding: 0px;
     position: absolute;
     border-radius: 3px;
   }
   
   div.out_prompt_overlay:hover {
     /* use inner shadow to get border that is computed the same on WebKit/FF */
     box-shadow: inset 0 0 1px #000;
     background: rgba(240, 240, 240, 0.5);
   }
   
   div.output_prompt {
       color: darkred;
       /* 5px right shift to account for margin in parent container */
       margin: 0 5px 0 -5px;
   }
   
   /* This class is the outer container of all output sections. */
   div.output_area {
       padding: 0px;
       page-break-inside: avoid;
   }
   
   /* This class is for the output subarea inside the output_area and after
      the prompt div. */
   div.output_subarea {
       padding: 0.4em 0.4em 0.4em 0.4em;
   }
   
   /* The rest of the output_* classes are for special styling of the different
      output types */
   
   /* all text output has this class: */
   div.output_text {
       text-align: left;
       color: black;
       font-family: monospace;
   }
   
   /* stdout/stderr are 'text' as well as 'stream', but pyout/pyerr are *not* streams */
   div.output_stream {
       padding-top: 0.0em;
       padding-bottom: 0.0em;
   }
   div.output_stdout {
   }
   div.output_stderr {
       background: #fdd; /* very light red background for stderr */
   }
   
   div.output_latex {
       text-align: left;
       color: black;
   }
   
   div.output_html {
   }
   
   div.output_png {
   }
   
   div.output_jpeg {
   }
   
   div.text_cell {
       background-color: white;
       padding: 5px 5px 5px 5px;
   }
   
   div.text_cell_input {
       color: black;
       border: 1px solid #ddd;
       border-radius: 3px;
       background: #f7f7f7;
   }
   
   div.text_cell_render {
       font-family: "Helvetica Neue", Arial, Helvetica, Geneva, sans-serif;
       outline: none;
       resize: none;
       width:  inherit;
       border-style: none;
       padding: 5px;
       color: black;
   }
   
   /* The following gets added to the <head> if it is detected that the user has a
    * monospace font with inconsistent normal/bold/italic height.  See
    * notebookmain.js.  Such fonts will have keywords vertically offset with
    * respect to the rest of the text.  The user should select a better font. 
    * See: https://github.com/ipython/ipython/issues/1503
    *
    * .CodeMirror span {
    *      vertical-align: bottom;
    * }
    */
   
   .CodeMirror {
       line-height: 1.231;  /* Changed from 1em to our global default */
   }
   
   .CodeMirror-scroll {
       height: auto;     /* Changed to auto to autogrow */
       /*  The CodeMirror docs are a bit fuzzy on if overflow-y should be hidden or visible.*/
       /*  We have found that if it is visible, vertical scrollbars appear with font size changes.*/
       overflow-y: hidden;
       overflow-x: auto; /* Changed from auto to remove scrollbar */
   }
   
   /* CSS font colors for translated ANSI colors. */
   
   
   .ansiblack {color: black;}
   .ansired {color: darkred;}
   .ansigreen {color: darkgreen;}
   .ansiyellow {color: brown;}
   .ansiblue {color: darkblue;}
   .ansipurple {color: darkviolet;}
   .ansicyan {color: steelblue;}
   .ansigrey {color: grey;}
   .ansibold {font-weight: bold;}
   
   .completions {
       position: absolute;
       z-index: 10;
       overflow: hidden;
       border: 1px solid grey;
   }
   
   .completions select {
       background: white;
       outline: none;
       border: none;
       padding: 0px;
       margin: 0px;
       overflow: auto;
       font-family: monospace;
   }
   
   option.context {
     background-color: #DEF7FF;
   }
   option.introspection {
     background-color: #EBF4EB;
   }
   
   /*fixed part of the completion*/
   .completions p b {
       font-weight:bold;
   }
   
   .completions p {
       background: #DDF;
       /*outline: none;
       padding: 0px;*/
       border-bottom: black solid 1px;
       padding: 1px;
       font-family: monospace;
   }
   
   pre.dialog {
       background-color: #f7f7f7;
       border: 1px solid #ddd;
       border-radius: 3px;
       padding: 0.4em;
       padding-left: 2em;
   }
   
   p.dialog {
       padding : 0.2em;
   }
   
   .shortcut_key {
       display: inline-block;
       width: 15ex;
       text-align: right;
       font-family: monospace;
   }
   
   .shortcut_descr {
   }
   
   /* Word-wrap output correctly.  This is the CSS3 spelling, though Firefox seems
      to not honor it correctly.  Webkit browsers (Chrome, rekonq, Safari) do.
    */
   pre, code, kbd, samp { white-space: pre-wrap; }
   
   #fonttest {
       font-family: monospace;
   }
   
   .js-error {
       color: darkred;
   }
   </style>
   <style type="text/css">
   .rendered_html {color: black;}
   .rendered_html em {font-style: italic;}
   .rendered_html strong {font-weight: bold;}
   .rendered_html u {text-decoration: underline;}
   .rendered_html :link { text-decoration: underline }
   .rendered_html :visited { text-decoration: underline }
   .rendered_html h1 {font-size: 197%; margin: .65em 0; font-weight: bold;}
   .rendered_html h2 {font-size: 153.9%; margin: .75em 0; font-weight: bold;}
   .rendered_html h3 {font-size: 123.1%; margin: .85em 0; font-weight: bold;}
   .rendered_html h4 {font-size: 100% margin: 0.95em 0; font-weight: bold;}
   .rendered_html h5 {font-size: 85%; margin: 1.5em 0; font-weight: bold;}
   .rendered_html h6 {font-size: 77%; margin: 1.65em 0; font-weight: bold;}
   .rendered_html ul {list-style:disc; margin: 1em 2em;}
   .rendered_html ul ul {list-style:square; margin: 0em 2em;}
   .rendered_html ul ul ul {list-style:circle; margin-left: 0em 2em;}
   .rendered_html ol {list-style:upper-roman; margin: 1em 2em;}
   .rendered_html ol ol {list-style:upper-alpha; margin: 0em 2em;}
   .rendered_html ol ol ol {list-style:decimal; margin: 0em 2em;}
   .rendered_html ol ol ol ol {list-style:lower-alpha; margin 0em 2em;}
   .rendered_html ol ol ol ol ol {list-style:lower-roman; 0em 2em;}
   
   .rendered_html hr {
       color: black;
       background-color: black;
   }
   
   .rendered_html pre {
       margin: 1em 2em;
   }
   
   .rendered_html blockquote {
       margin: 1em 2em;
   }
   
   .rendered_html table {
       border: 1px solid black;
       border-collapse: collapse;
       margin: 1em 2em;
   }
   
   .rendered_html td {
       border: 1px solid black;
       text-align: left;
       vertical-align: middle;
       padding: 4px;
   }
   
   .rendered_html th {
       border: 1px solid black;
       text-align: left;
       vertical-align: middle;
       padding: 4px;
       font-weight: bold;
   }
   
   .rendered_html tr {
       border: 1px solid black;
   }    
   
   .rendered_html p + p {
       margin-top: 1em;
   }
   
   
   </style>
   <style type="text/css">
   /* Overrides of notebook CSS for static HTML export
   
   */
   div.ipynb {
     overflow: visible;
     padding: 8px;
   }
   .input_area {
     padding: 0.4em;
   }
   
   </style>
   <meta charset="UTF-8">
   <style type="text/css">
   .highlight-ipynb .hll { background-color: #ffffcc }
   .highlight-ipynb  { background: #f8f8f8; }
   .highlight-ipynb .c { color: #408080; font-style: italic } /* Comment */
   .highlight-ipynb .err { border: 1px solid #FF0000 } /* Error */
   .highlight-ipynb .k { color: #008000; font-weight: bold } /* Keyword */
   .highlight-ipynb .o { color: #666666 } /* Operator */
   .highlight-ipynb .cm { color: #408080; font-style: italic } /* Comment.Multiline */
   .highlight-ipynb .cp { color: #BC7A00 } /* Comment.Preproc */
   .highlight-ipynb .c1 { color: #408080; font-style: italic } /* Comment.Single */
   .highlight-ipynb .cs { color: #408080; font-style: italic } /* Comment.Special */
   .highlight-ipynb .gd { color: #A00000 } /* Generic.Deleted */
   .highlight-ipynb .ge { font-style: italic } /* Generic.Emph */
   .highlight-ipynb .gr { color: #FF0000 } /* Generic.Error */
   .highlight-ipynb .gh { color: #000080; font-weight: bold } /* Generic.Heading */
   .highlight-ipynb .gi { color: #00A000 } /* Generic.Inserted */
   .highlight-ipynb .go { color: #888888 } /* Generic.Output */
   .highlight-ipynb .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
   .highlight-ipynb .gs { font-weight: bold } /* Generic.Strong */
   .highlight-ipynb .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
   .highlight-ipynb .gt { color: #0044DD } /* Generic.Traceback */
   .highlight-ipynb .kc { color: #008000; font-weight: bold } /* Keyword.Constant */
   .highlight-ipynb .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
   .highlight-ipynb .kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
   .highlight-ipynb .kp { color: #008000 } /* Keyword.Pseudo */
   .highlight-ipynb .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
   .highlight-ipynb .kt { color: #B00040 } /* Keyword.Type */
   .highlight-ipynb .m { color: #666666 } /* Literal.Number */
   .highlight-ipynb .s { color: #BA2121 } /* Literal.String */
   .highlight-ipynb .na { color: #7D9029 } /* Name.Attribute */
   .highlight-ipynb .nb { color: #008000 } /* Name.Builtin */
   .highlight-ipynb .nc { color: #0000FF; font-weight: bold } /* Name.Class */
   .highlight-ipynb .no { color: #880000 } /* Name.Constant */
   .highlight-ipynb .nd { color: #AA22FF } /* Name.Decorator */
   .highlight-ipynb .ni { color: #999999; font-weight: bold } /* Name.Entity */
   .highlight-ipynb .ne { color: #D2413A; font-weight: bold } /* Name.Exception */
   .highlight-ipynb .nf { color: #0000FF } /* Name.Function */
   .highlight-ipynb .nl { color: #A0A000 } /* Name.Label */
   .highlight-ipynb .nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
   .highlight-ipynb .nt { color: #008000; font-weight: bold } /* Name.Tag */
   .highlight-ipynb .nv { color: #19177C } /* Name.Variable */
   .highlight-ipynb .ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
   .highlight-ipynb .w { color: #bbbbbb } /* Text.Whitespace */
   .highlight-ipynb .mf { color: #666666 } /* Literal.Number.Float */
   .highlight-ipynb .mh { color: #666666 } /* Literal.Number.Hex */
   .highlight-ipynb .mi { color: #666666 } /* Literal.Number.Integer */
   .highlight-ipynb .mo { color: #666666 } /* Literal.Number.Oct */
   .highlight-ipynb .sb { color: #BA2121 } /* Literal.String.Backtick */
   .highlight-ipynb .sc { color: #BA2121 } /* Literal.String.Char */
   .highlight-ipynb .sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
   .highlight-ipynb .s2 { color: #BA2121 } /* Literal.String.Double */
   .highlight-ipynb .se { color: #BB6622; font-weight: bold } /* Literal.String.Escape */
   .highlight-ipynb .sh { color: #BA2121 } /* Literal.String.Heredoc */
   .highlight-ipynb .si { color: #BB6688; font-weight: bold } /* Literal.String.Interpol */
   .highlight-ipynb .sx { color: #008000 } /* Literal.String.Other */
   .highlight-ipynb .sr { color: #BB6688 } /* Literal.String.Regex */
   .highlight-ipynb .s1 { color: #BA2121 } /* Literal.String.Single */
   .highlight-ipynb .ss { color: #19177C } /* Literal.String.Symbol */
   .highlight-ipynb .bp { color: #008000 } /* Name.Builtin.Pseudo */
   .highlight-ipynb .vc { color: #19177C } /* Name.Variable.Class */
   .highlight-ipynb .vg { color: #19177C } /* Name.Variable.Global */
   .highlight-ipynb .vi { color: #19177C } /* Name.Variable.Instance */
   .highlight-ipynb .il { color: #666666 } /* Literal.Number.Integer.Long */
   </style>

   <div class="ipynb">
   <div class="text_cell_render border-box-sizing rendered_html">

   <p>We've been working on a <a href="https://github.com/gilbertgede/idetc-2013-paper">conference paper</a> to demonstrate the ability to do multibody dynamics with Python. We've been calling this work flow <a href="http://pydy.org">PyDy</a>, short for Python Dynamics. Several pieces of the puzzle have come together lately to really demonstrate the power of the scientific python software packages to handle complex dynamic and controls problems (i.e. IPython notebooks, matplotlib animations, python-control, and our software package mechanics which is a part of SymPy). After writing the draft of our paper, which uses a general n-link pendulum as it's main example, I came across this <a href="http://blog.wolfram.com/2011/03/01/stabilized-n-link-pendulum/">blog post by Wolfram</a> demonstrating their ability to symbolically derive the equations of motion for the n-link pendulum and stabilize it with an LQR controller. It inspired me to replicate the example as I realized that it was relatively easy to do with all free and open source software!</p>

   <p>In this example problem we will derive the equations of motion of an n-link pendulum on a laterally sliding cart and then develop a controller to stabilize it. Balancing a single inverted pendulum is a classic problem that is many times a student's first experience with non-linear dynamics and control. The problem here is extended to a general n-link pendulum and as we will see the equations of motion quickly get messy with greater than 2 links.</p>
   <p>The diagram below shows the general description of the problem.</p>
   </div>
   <div class="cell border-box-sizing code_cell vbox">
   <div class="input hbox">
   <div class="prompt input_prompt">In&nbsp;[1]:</div>
   <div class="input_area box-flex1">
   <div class="highlight-ipynb"><pre class="ipynb"><span class="kn">from</span> <span class="nn">IPython.display</span> <span class="kn">import</span> <span class="n">SVG</span>
   <span class="n">SVG</span><span class="p">(</span><span class="n">filename</span><span class="o">=</span><span class="s">&#39;n-pendulum-with-cart.svg&#39;</span><span class="p">)</span>
   </pre></div>

   </div>
   </div>
   <div class="vbox output_wrapper">
   <div class="output vbox">
   <div class="hbox output_area">
   <div class="prompt output_prompt">Out[1]:</div>
   <div class="output_subarea output_pyout">
   <svg height="270" id="svg2" inkscape:version="0.48.3.1 r9886" sodipodi:docname="n-pendulum-with-cart.svg" version="1.1" width="360" xmlns="http://www.w3.org/2000/svg" xmlns:cc="http://creativecommons.org/ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" xmlns:ns0="http://www.iki.fi/pav/software/textext/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd" xmlns:svg="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
     <sodipodi:namedview bordercolor="#666666" borderopacity="1.0" id="base" inkscape:current-layer="layer1" inkscape:cx="180" inkscape:cy="180" inkscape:document-units="px" inkscape:pageopacity="0.0" inkscape:pageshadow="2" inkscape:window-height="744" inkscape:window-maximized="1" inkscape:window-width="1366" inkscape:window-x="0" inkscape:window-y="24" inkscape:zoom="1.5694444" pagecolor="#ffffff" showgrid="false" units="in"/>
     <defs id="defs4">
       <marker id="Arrow1Send" inkscape:stockid="Arrow1Send" orient="auto" refX="0" refY="0" style="overflow:visible">
         <path d="M 0,0 5,-5 -12.5,0 5,5 0,0 z" id="path4056" inkscape:connector-curvature="0" style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" transform="matrix(-0.2,0,0,-0.2,-1.2,0)"/>
       </marker>
       <marker id="Arrow1Sstart" inkscape:stockid="Arrow1Sstart" orient="auto" refX="0" refY="0" style="overflow:visible">
         <path d="M 0,0 5,-5 -12.5,0 5,5 0,0 z" id="path4053" inkscape:connector-curvature="0" style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" transform="matrix(0.2,0,0,0.2,1.2,0)"/>
       </marker>
       <marker id="Arrow1Mend" inkscape:stockid="Arrow1Mend" orient="auto" refX="0" refY="0" style="overflow:visible">
         <path d="M 0,0 5,-5 -12.5,0 5,5 0,0 z" id="path4050" inkscape:connector-curvature="0" style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" transform="matrix(-0.4,0,0,-0.4,-4,0)"/>
       </marker>
       <marker id="Arrow1Mstart" inkscape:stockid="Arrow1Mstart" orient="auto" refX="0" refY="0" style="overflow:visible">
         <path d="M 0,0 5,-5 -12.5,0 5,5 0,0 z" id="path4047" inkscape:connector-curvature="0" style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" transform="matrix(0.4,0,0,0.4,4,0)"/>
       </marker>
       <marker id="Arrow1Sstart-7" inkscape:stockid="Arrow1Sstart" orient="auto" refX="0" refY="0" style="overflow:visible">
         <path d="M 0,0 5,-5 -12.5,0 5,5 0,0 z" id="path4053-9" inkscape:connector-curvature="0" style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" transform="matrix(0.2,0,0,0.2,1.2,0)"/>
       </marker>
       <marker id="Arrow1Sstart-8" inkscape:stockid="Arrow1Sstart" orient="auto" refX="0" refY="0" style="overflow:visible">
         <path d="M 0,0 5,-5 -12.5,0 5,5 0,0 z" id="path4053-98" inkscape:connector-curvature="0" style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt" transform="matrix(0.2,0,0,0.2,1.2,0)"/>
       </marker>
     </defs>
     <metadata id="metadata7">
       <rdf:RDF>
         <cc:Work rdf:about="">
           <dc:format>image/svg+xml</dc:format>
           <dc:type rdf:resource="http://purl.org/dc/dcmitype/StillImage"/>
           <dc:title/>
         </cc:Work>
       </rdf:RDF>
     </metadata>
     <g id="layer1" inkscape:groupmode="layer" inkscape:label="Layer 1" transform="translate(0,-782.35975)">
       <rect height="20.389381" id="rect2985" style="fill:#ff0000;fill-opacity:1;stroke:#000000;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;stroke-dashoffset:0" width="95.575218" x="119.11504" y="991.19159"/>
       <path d="m 89.840708,1002.0235 -50.336283,0 0,-50.33631" id="path2989" inkscape:connector-curvature="0" style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1;marker-start:url(#Arrow1Mstart);marker-end:url(#Arrow1Mend)"/>
       <path d="m 167.57522,1001.3863 72.53954,-41.88072" id="path2993" inkscape:connector-curvature="0" style="fill:none;stroke:#0000ff;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none"/>
       <path d="m 240.3275,959.24943 54.56622,-63.54926" id="path2993-2" inkscape:connector-curvature="0" style="fill:none;stroke:#0000ff;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:2, 2;stroke-dashoffset:0"/>
       <path d="m 295.06598,895.13259 17.72644,-81.86424" id="path2993-6" inkscape:connector-curvature="0" style="fill:none;stroke:#0000ff;stroke-width:2;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none"/>
       <path d="m 89.840708,151.00885 c 0,8.09366 -6.418573,14.65487 -14.336283,14.65487 -7.91771,0 -14.336283,-6.56121 -14.336283,-14.65487 0,-8.09366 6.418573,-14.65487 14.336283,-14.65487 7.91771,0 14.336283,6.56121 14.336283,14.65487 z" id="path3020" sodipodi:cx="75.504425" sodipodi:cy="151.00885" sodipodi:rx="14.336283" sodipodi:ry="14.654867" sodipodi:type="arc" style="fill:#0000ff;fill-opacity:1;stroke:none" transform="matrix(0.52314816,0,0,0.51177538,200.53296,882.26204)"/>
       <path d="m 176.98476,1002.0235 56.70796,0" id="path3022" inkscape:connector-curvature="0" sodipodi:nodetypes="cc" style="fill:none;stroke:#000000;stroke-width:1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:3, 3;stroke-dashoffset:0"/>
       <path d="m 250.58043,960.83281 41.36951,0" id="path3024" inkscape:connector-curvature="0" sodipodi:nodetypes="cc" style="fill:none;stroke:#000000;stroke-width:1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:3, 3;stroke-dashoffset:0;marker-start:none"/>
       <path d="m 304.86894,896.40815 19.07525,0" id="path3026" inkscape:connector-curvature="0" sodipodi:nodetypes="cc" style="fill:none;stroke:#000000;stroke-width:1;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:3, 3;stroke-dashoffset:0"/>
       <path d="m 89.840708,151.00885 c 0,8.09366 -6.418573,14.65487 -14.336283,14.65487 -7.91771,0 -14.336283,-6.56121 -14.336283,-14.65487 0,-8.09366 6.418573,-14.65487 14.336283,-14.65487 7.91771,0 14.336283,6.56121 14.336283,14.65487 z" id="path3020-0" sodipodi:cx="75.504425" sodipodi:cy="151.00885" sodipodi:rx="14.336283" sodipodi:ry="14.654867" sodipodi:type="arc" style="fill:#0000ff;fill-opacity:1;stroke:none" transform="matrix(0.52314816,0,0,0.51177538,128.46306,924.42824)"/>
       <path d="m 89.840708,151.00885 c 0,8.09366 -6.418573,14.65487 -14.336283,14.65487 -7.91771,0 -14.336283,-6.56121 -14.336283,-14.65487 0,-8.09366 6.418573,-14.65487 14.336283,-14.65487 7.91771,0 14.336283,6.56121 14.336283,14.65487 z" id="path3020-7" sodipodi:cx="75.504425" sodipodi:cy="151.00885" sodipodi:rx="14.336283" sodipodi:ry="14.654867" sodipodi:type="arc" style="fill:#0000ff;fill-opacity:1;stroke:none" transform="matrix(0.52314816,0,0,0.51177538,254.84119,819.0005)"/>
       <path d="m 89.840708,151.00885 c 0,8.09366 -6.418573,14.65487 -14.336283,14.65487 -7.91771,0 -14.336283,-6.56121 -14.336283,-14.65487 0,-8.09366 6.418573,-14.65487 14.336283,-14.65487 7.91771,0 14.336283,6.56121 14.336283,14.65487 z" id="path3020-06" sodipodi:cx="75.504425" sodipodi:cy="151.00885" sodipodi:rx="14.336283" sodipodi:ry="14.654867" sodipodi:type="arc" style="fill:#0000ff;fill-opacity:1;stroke:none" transform="matrix(0.52314816,0,0,0.51177538,273.53884,736.77587)"/>
       <g id="g4707" ns0:preamble="" ns0:text="$O$" transform="translate(-193.76468,875.86895)">
         <defs id="defs4709">
           <g id="g4711">
             <symbol id="textext-d3625bf8-0" overflow="visible" style="overflow:visible">
               <path d="" id="path4714" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-d3625bf8-1" overflow="visible" style="overflow:visible">
               <path d="m 7.375,-4.34375 c 0,-1.609375 -1.0625,-2.6875 -2.546875,-2.6875 -2.140625,0 -4.34375,2.265625 -4.34375,4.59375 0,1.65625 1.125,2.65625 2.5625,2.65625 2.109375,0 4.328125,-2.1875 4.328125,-4.5625 z m -4.28125,4.296875 c -0.984375,0 -1.671875,-0.796875 -1.671875,-2.109375 0,-0.453125 0.140625,-1.90625 0.90625,-3.0625 0.6875,-1.046875 1.65625,-1.5625 2.453125,-1.5625 0.8125,0 1.703125,0.5625 1.703125,2.046875 0,0.71875 -0.265625,2.265625 -1.25,3.5 C 4.75,-0.625 3.9375,-0.046875 3.09375,-0.046875 z" id="path4717" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
           </g>
         </defs>
         <g id="textext-d3625bf8-2">
           <g id="g4720" style="fill:#000000;fill-opacity:1">
             <use height="360" id="use4722" width="360" x="223.43201" xlink:href="#textext-d3625bf8-1" y="134.765"/>
           </g>
         </g>
       </g>
       <g id="g4784" ns0:preamble="" ns0:text="$q_0$" transform="translate(-124.10822,898.97412)">
         <defs id="defs4786">
           <g id="g4788">
             <symbol id="textext-7b8382d5-0" overflow="visible" style="overflow:visible">
               <path d="" id="path4791" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-7b8382d5-1" overflow="visible" style="overflow:visible">
               <path d="m 4.5,-4.296875 c 0,-0.046875 -0.03125,-0.09375 -0.09375,-0.09375 -0.109375,0 -0.515625,0.390625 -0.671875,0.6875 C 3.515625,-4.25 3.125,-4.40625 2.796875,-4.40625 c -1.171875,0 -2.390625,1.46875 -2.390625,2.921875 0,0.96875 0.578125,1.59375 1.3125,1.59375 0.421875,0 0.8125,-0.234375 1.171875,-0.59375 -0.09375,0.34375 -0.421875,1.6875 -0.453125,1.78125 -0.078125,0.28125 -0.15625,0.3125 -0.71875,0.328125 -0.125,0 -0.21875,0 -0.21875,0.203125 0,0 0,0.109375 0.125,0.109375 0.3125,0 0.671875,-0.03125 1,-0.03125 0.328125,0 0.6875,0.03125 1.03125,0.03125 0.046875,0 0.171875,0 0.171875,-0.203125 C 3.828125,1.625 3.734375,1.625 3.5625,1.625 3.09375,1.625 3.09375,1.5625 3.09375,1.46875 3.09375,1.390625 3.109375,1.328125 3.125,1.25 z m -2.75,4.1875 c -0.609375,0 -0.640625,-0.765625 -0.640625,-0.9375 0,-0.484375 0.28125,-1.5625 0.453125,-1.984375 0.3125,-0.734375 0.828125,-1.15625 1.234375,-1.15625 0.65625,0 0.796875,0.8125 0.796875,0.875 0,0.0625 -0.546875,2.25 -0.578125,2.28125 C 2.859375,-0.75 2.296875,-0.109375 1.75,-0.109375 z" id="path4794" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-7b8382d5-2" overflow="visible" style="overflow:visible">
               <path d="" id="path4797" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-7b8382d5-3" overflow="visible" style="overflow:visible">
               <path d="M 3.59375,-2.21875 C 3.59375,-2.984375 3.5,-3.546875 3.1875,-4.03125 2.96875,-4.34375 2.53125,-4.625 1.984375,-4.625 c -1.625,0 -1.625,1.90625 -1.625,2.40625 0,0.5 0,2.359375 1.625,2.359375 1.609375,0 1.609375,-1.859375 1.609375,-2.359375 z M 1.984375,-0.0625 c -0.328125,0 -0.75,-0.1875 -0.890625,-0.75 C 1,-1.21875 1,-1.796875 1,-2.3125 1,-2.828125 1,-3.359375 1.09375,-3.734375 1.25,-4.28125 1.6875,-4.4375 1.984375,-4.4375 c 0.375,0 0.734375,0.234375 0.859375,0.640625 0.109375,0.375 0.125,0.875 0.125,1.484375 0,0.515625 0,1.03125 -0.09375,1.46875 -0.140625,0.640625 -0.609375,0.78125 -0.890625,0.78125 z" id="path4800" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
           </g>
         </defs>
         <g id="textext-7b8382d5-4">
           <g id="g4803" style="fill:#000000;fill-opacity:1">
             <use height="360" id="use4805" width="360" x="223.43201" xlink:href="#textext-7b8382d5-1" y="134.765"/>
           </g>
           <g id="g4807" style="fill:#000000;fill-opacity:1">
             <use height="360" id="use4809" width="360" x="227.88" xlink:href="#textext-7b8382d5-3" y="136.259"/>
           </g>
         </g>
       </g>
       <g id="g4903" ns0:preamble="" ns0:text="$q_1$" transform="translate(5.8089688,851.4691)">
         <defs id="defs4905">
           <g id="g4907">
             <symbol id="textext-d862ba06-0" overflow="visible" style="overflow:visible">
               <path d="" id="path4910" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-d862ba06-1" overflow="visible" style="overflow:visible">
               <path d="m 4.5,-4.296875 c 0,-0.046875 -0.03125,-0.09375 -0.09375,-0.09375 -0.109375,0 -0.515625,0.390625 -0.671875,0.6875 C 3.515625,-4.25 3.125,-4.40625 2.796875,-4.40625 c -1.171875,0 -2.390625,1.46875 -2.390625,2.921875 0,0.96875 0.578125,1.59375 1.3125,1.59375 0.421875,0 0.8125,-0.234375 1.171875,-0.59375 -0.09375,0.34375 -0.421875,1.6875 -0.453125,1.78125 -0.078125,0.28125 -0.15625,0.3125 -0.71875,0.328125 -0.125,0 -0.21875,0 -0.21875,0.203125 0,0 0,0.109375 0.125,0.109375 0.3125,0 0.671875,-0.03125 1,-0.03125 0.328125,0 0.6875,0.03125 1.03125,0.03125 0.046875,0 0.171875,0 0.171875,-0.203125 C 3.828125,1.625 3.734375,1.625 3.5625,1.625 3.09375,1.625 3.09375,1.5625 3.09375,1.46875 3.09375,1.390625 3.109375,1.328125 3.125,1.25 z m -2.75,4.1875 c -0.609375,0 -0.640625,-0.765625 -0.640625,-0.9375 0,-0.484375 0.28125,-1.5625 0.453125,-1.984375 0.3125,-0.734375 0.828125,-1.15625 1.234375,-1.15625 0.65625,0 0.796875,0.8125 0.796875,0.875 0,0.0625 -0.546875,2.25 -0.578125,2.28125 C 2.859375,-0.75 2.296875,-0.109375 1.75,-0.109375 z" id="path4913" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-d862ba06-2" overflow="visible" style="overflow:visible">
               <path d="" id="path4916" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-d862ba06-3" overflow="visible" style="overflow:visible">
               <path d="m 2.328125,-4.4375 c 0,-0.1875 0,-0.1875 -0.203125,-0.1875 -0.453125,0.4375 -1.078125,0.4375 -1.359375,0.4375 l 0,0.25 c 0.15625,0 0.625,0 1,-0.1875 l 0,3.546875 c 0,0.234375 0,0.328125 -0.6875,0.328125 l -0.265625,0 0,0.25 c 0.125,0 0.984375,-0.03125 1.234375,-0.03125 0.21875,0 1.09375,0.03125 1.25,0.03125 l 0,-0.25 -0.265625,0 c -0.703125,0 -0.703125,-0.09375 -0.703125,-0.328125 z" id="path4919" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
           </g>
         </defs>
         <g id="textext-d862ba06-4">
           <g id="g4922" style="fill:#000000;fill-opacity:1">
             <use height="360" id="use4924" width="360" x="223.43201" xlink:href="#textext-d862ba06-1" y="134.765"/>
           </g>
           <g id="g4926" style="fill:#000000;fill-opacity:1">
             <use height="360" id="use4928" width="360" x="227.88" xlink:href="#textext-d862ba06-3" y="136.259"/>
           </g>
         </g>
       </g>
       <g id="g5054" ns0:preamble="" ns0:text="$q_2$" transform="translate(61.774552,807.35558)">
         <defs id="defs5056">
           <g id="g5058">
             <symbol id="textext-726c0b90-0" overflow="visible" style="overflow:visible">
               <path d="" id="path5061" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-726c0b90-1" overflow="visible" style="overflow:visible">
               <path d="m 4.5,-4.296875 c 0,-0.046875 -0.03125,-0.09375 -0.09375,-0.09375 -0.109375,0 -0.515625,0.390625 -0.671875,0.6875 C 3.515625,-4.25 3.125,-4.40625 2.796875,-4.40625 c -1.171875,0 -2.390625,1.46875 -2.390625,2.921875 0,0.96875 0.578125,1.59375 1.3125,1.59375 0.421875,0 0.8125,-0.234375 1.171875,-0.59375 -0.09375,0.34375 -0.421875,1.6875 -0.453125,1.78125 -0.078125,0.28125 -0.15625,0.3125 -0.71875,0.328125 -0.125,0 -0.21875,0 -0.21875,0.203125 0,0 0,0.109375 0.125,0.109375 0.3125,0 0.671875,-0.03125 1,-0.03125 0.328125,0 0.6875,0.03125 1.03125,0.03125 0.046875,0 0.171875,0 0.171875,-0.203125 C 3.828125,1.625 3.734375,1.625 3.5625,1.625 3.09375,1.625 3.09375,1.5625 3.09375,1.46875 3.09375,1.390625 3.109375,1.328125 3.125,1.25 z m -2.75,4.1875 c -0.609375,0 -0.640625,-0.765625 -0.640625,-0.9375 0,-0.484375 0.28125,-1.5625 0.453125,-1.984375 0.3125,-0.734375 0.828125,-1.15625 1.234375,-1.15625 0.65625,0 0.796875,0.8125 0.796875,0.875 0,0.0625 -0.546875,2.25 -0.578125,2.28125 C 2.859375,-0.75 2.296875,-0.109375 1.75,-0.109375 z" id="path5064" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-726c0b90-2" overflow="visible" style="overflow:visible">
               <path d="" id="path5067" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-726c0b90-3" overflow="visible" style="overflow:visible">
               <path d="m 3.515625,-1.265625 -0.234375,0 c -0.015625,0.15625 -0.09375,0.5625 -0.1875,0.625 -0.046875,0.046875 -0.578125,0.046875 -0.6875,0.046875 l -1.28125,0 c 0.734375,-0.640625 0.984375,-0.84375 1.390625,-1.171875 0.515625,-0.40625 1,-0.84375 1,-1.5 0,-0.84375 -0.734375,-1.359375 -1.625,-1.359375 -0.859375,0 -1.453125,0.609375 -1.453125,1.25 0,0.34375 0.296875,0.390625 0.375,0.390625 0.15625,0 0.359375,-0.125 0.359375,-0.375 0,-0.125 -0.046875,-0.375 -0.40625,-0.375 C 0.984375,-4.21875 1.453125,-4.375 1.78125,-4.375 c 0.703125,0 1.0625,0.546875 1.0625,1.109375 0,0.609375 -0.4375,1.078125 -0.65625,1.328125 L 0.515625,-0.265625 C 0.4375,-0.203125 0.4375,-0.1875 0.4375,0 l 2.875,0 z" id="path5070" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
           </g>
         </defs>
         <g id="textext-726c0b90-4">
           <g id="g5073" style="fill:#000000;fill-opacity:1">
             <use height="360" id="use5075" width="360" x="223.43201" xlink:href="#textext-726c0b90-1" y="134.765"/>
           </g>
           <g id="g5077" style="fill:#000000;fill-opacity:1">
             <use height="360" id="use5079" width="360" x="227.88" xlink:href="#textext-726c0b90-3" y="136.259"/>
           </g>
         </g>
       </g>
       <g id="g5237" ns0:preamble="" ns0:text="$q_{n+1}$" transform="translate(94.233787,742.30109)">
         <defs id="defs5239">
           <g id="g5241">
             <symbol id="textext-fcfaf03e-0" overflow="visible" style="overflow:visible">
               <path d="" id="path5244" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-fcfaf03e-1" overflow="visible" style="overflow:visible">
               <path d="m 4.5,-4.296875 c 0,-0.046875 -0.03125,-0.09375 -0.09375,-0.09375 -0.109375,0 -0.515625,0.390625 -0.671875,0.6875 C 3.515625,-4.25 3.125,-4.40625 2.796875,-4.40625 c -1.171875,0 -2.390625,1.46875 -2.390625,2.921875 0,0.96875 0.578125,1.59375 1.3125,1.59375 0.421875,0 0.8125,-0.234375 1.171875,-0.59375 -0.09375,0.34375 -0.421875,1.6875 -0.453125,1.78125 -0.078125,0.28125 -0.15625,0.3125 -0.71875,0.328125 -0.125,0 -0.21875,0 -0.21875,0.203125 0,0 0,0.109375 0.125,0.109375 0.3125,0 0.671875,-0.03125 1,-0.03125 0.328125,0 0.6875,0.03125 1.03125,0.03125 0.046875,0 0.171875,0 0.171875,-0.203125 C 3.828125,1.625 3.734375,1.625 3.5625,1.625 3.09375,1.625 3.09375,1.5625 3.09375,1.46875 3.09375,1.390625 3.109375,1.328125 3.125,1.25 z m -2.75,4.1875 c -0.609375,0 -0.640625,-0.765625 -0.640625,-0.9375 0,-0.484375 0.28125,-1.5625 0.453125,-1.984375 0.3125,-0.734375 0.828125,-1.15625 1.234375,-1.15625 0.65625,0 0.796875,0.8125 0.796875,0.875 0,0.0625 -0.546875,2.25 -0.578125,2.28125 C 2.859375,-0.75 2.296875,-0.109375 1.75,-0.109375 z" id="path5247" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-fcfaf03e-2" overflow="visible" style="overflow:visible">
               <path d="" id="path5250" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-fcfaf03e-3" overflow="visible" style="overflow:visible">
               <path d="m 0.84375,-0.4375 c -0.015625,0.09375 -0.0625,0.265625 -0.0625,0.28125 0,0.15625 0.125,0.21875 0.234375,0.21875 0.125,0 0.234375,-0.078125 0.28125,-0.140625 0.03125,-0.0625 0.078125,-0.296875 0.125,-0.4375 0.03125,-0.125 0.109375,-0.453125 0.140625,-0.625 0.046875,-0.15625 0.09375,-0.3125 0.125,-0.46875 0.078125,-0.28125 0.09375,-0.34375 0.296875,-0.625 C 2.171875,-2.515625 2.5,-2.875 3.03125,-2.875 c 0.390625,0 0.40625,0.359375 0.40625,0.484375 0,0.421875 -0.296875,1.1875 -0.40625,1.484375 -0.078125,0.203125 -0.109375,0.265625 -0.109375,0.375 0,0.375 0.296875,0.59375 0.65625,0.59375 0.703125,0 1,-0.953125 1,-1.0625 0,-0.09375 -0.078125,-0.09375 -0.109375,-0.09375 -0.09375,0 -0.09375,0.046875 -0.125,0.125 C 4.1875,-0.40625 3.875,-0.125 3.609375,-0.125 c -0.15625,0 -0.1875,-0.09375 -0.1875,-0.25 0,-0.15625 0.046875,-0.25 0.171875,-0.5625 0.078125,-0.21875 0.359375,-0.953125 0.359375,-1.34375 0,-0.671875 -0.53125,-0.796875 -0.90625,-0.796875 -0.578125,0 -0.96875,0.359375 -1.171875,0.640625 -0.046875,-0.484375 -0.453125,-0.640625 -0.75,-0.640625 -0.296875,0 -0.453125,0.21875 -0.546875,0.375 -0.15625,0.265625 -0.25,0.65625 -0.25,0.703125 0,0.078125 0.09375,0.078125 0.125,0.078125 0.09375,0 0.09375,-0.015625 0.140625,-0.203125 0.109375,-0.40625 0.25,-0.75 0.515625,-0.75 0.1875,0 0.234375,0.15625 0.234375,0.34375 0,0.125 -0.0625,0.390625 -0.125,0.578125 -0.046875,0.1875 -0.109375,0.46875 -0.140625,0.625 z" id="path5253" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-fcfaf03e-4" overflow="visible" style="overflow:visible">
               <path d="" id="path5256" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-fcfaf03e-5" overflow="visible" style="overflow:visible">
               <path d="m 3.21875,-1.578125 2.140625,0 c 0.09375,0 0.25,0 0.25,-0.15625 0,-0.1875 -0.15625,-0.1875 -0.25,-0.1875 l -2.140625,0 0,-2.140625 c 0,-0.078125 0,-0.25 -0.15625,-0.25 -0.171875,0 -0.171875,0.15625 -0.171875,0.25 l 0,2.140625 -2.140625,0 c -0.09375,0 -0.265625,0 -0.265625,0.171875 0,0.171875 0.15625,0.171875 0.265625,0.171875 l 2.140625,0 0,2.140625 c 0,0.09375 0,0.265625 0.15625,0.265625 0.171875,0 0.171875,-0.171875 0.171875,-0.265625 z" id="path5259" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-fcfaf03e-6" overflow="visible" style="overflow:visible">
               <path d="m 2.328125,-4.4375 c 0,-0.1875 0,-0.1875 -0.203125,-0.1875 -0.453125,0.4375 -1.078125,0.4375 -1.359375,0.4375 l 0,0.25 c 0.15625,0 0.625,0 1,-0.1875 l 0,3.546875 c 0,0.234375 0,0.328125 -0.6875,0.328125 l -0.265625,0 0,0.25 c 0.125,0 0.984375,-0.03125 1.234375,-0.03125 0.21875,0 1.09375,0.03125 1.25,0.03125 l 0,-0.25 -0.265625,0 c -0.703125,0 -0.703125,-0.09375 -0.703125,-0.328125 z" id="path5262" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
           </g>
         </defs>
         <g id="textext-fcfaf03e-7">
           <g id="g5265" style="fill:#000000;fill-opacity:1">
             <use height="360" id="use5267" width="360" x="223.43201" xlink:href="#textext-fcfaf03e-1" y="134.765"/>
           </g>
           <g id="g5269" style="fill:#000000;fill-opacity:1">
             <use height="360" id="use5271" width="360" x="227.88" xlink:href="#textext-fcfaf03e-3" y="136.259"/>
           </g>
           <g id="g5273" style="fill:#000000;fill-opacity:1">
             <use height="360" id="use5275" width="360" x="232.804" xlink:href="#textext-fcfaf03e-5" y="136.259"/>
             <use height="360" id="use5277" width="360" x="238.92003" xlink:href="#textext-fcfaf03e-6" y="136.259"/>
           </g>
         </g>
       </g>
       <path d="m 122.76541,131.92575 c 3.01342,5.6626 4.6165,12.00011 4.66698,18.45013" id="path5381" sodipodi:cx="89.203537" sodipodi:cy="150.69026" sodipodi:end="6.2751625" sodipodi:open="true" sodipodi:rx="38.230087" sodipodi:ry="39.185841" sodipodi:start="5.7838302" sodipodi:type="arc" style="fill:none;stroke:#000000;stroke-width:0.68079019;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;marker-start:url(#Arrow1Sstart)" transform="matrix(1.4871292,0,0,1.4508575,35.30588,783.08076)"/>
       <path d="m 115.95234,122.69366 c 7.40666,7.4348 11.55003,17.63396 11.48042,28.25973" id="path5381-2" sodipodi:cx="89.203537" sodipodi:cy="150.69026" sodipodi:end="6.2899002" sodipodi:open="true" sodipodi:rx="38.230087" sodipodi:ry="39.185841" sodipodi:start="5.4873376" sodipodi:type="arc" style="fill:none;stroke:#000000;stroke-width:0.85336822;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;marker-start:url(#Arrow1Sstart)" transform="matrix(1.1863846,0,0,1.1574482,133.87429,785.12848)"/>
       <path d="m 101.40416,113.5535 c 15.28996,5.27755 25.70184,19.82559 26.02194,36.35929" id="path5381-26" sodipodi:cx="89.203537" sodipodi:cy="150.69026" sodipodi:end="6.2633433" sodipodi:open="true" sodipodi:rx="38.230087" sodipodi:ry="39.185841" sodipodi:start="5.0372073" sodipodi:type="arc" style="fill:none;stroke:#000000;stroke-width:1.46858275;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;marker-start:url(#Arrow1Sstart)" transform="matrix(0.68938773,0,0,0.67257328,232.65421,794.93287)"/>
       <g id="g6087" ns0:preamble="" ns0:text="$m_0$" transform="translate(-77.95156,864.12085)">
         <defs id="defs6089">
           <g id="g6091">
             <symbol id="textext-998f6c43-0" overflow="visible" style="overflow:visible">
               <path d="" id="path6094" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-998f6c43-1" overflow="visible" style="overflow:visible">
               <path d="m 0.875,-0.59375 c -0.03125,0.15625 -0.09375,0.390625 -0.09375,0.4375 0,0.171875 0.140625,0.265625 0.296875,0.265625 0.125,0 0.296875,-0.078125 0.375,-0.28125 0,-0.015625 0.125,-0.484375 0.1875,-0.734375 l 0.21875,-0.890625 C 1.90625,-2.03125 1.96875,-2.25 2.03125,-2.46875 c 0.03125,-0.171875 0.109375,-0.46875 0.125,-0.5 0.140625,-0.3125 0.671875,-1.21875 1.625,-1.21875 0.453125,0 0.53125,0.375 0.53125,0.703125 0,0.25 -0.0625,0.53125 -0.140625,0.828125 L 3.890625,-1.5 3.6875,-0.75 c -0.03125,0.203125 -0.125,0.546875 -0.125,0.59375 0,0.171875 0.140625,0.265625 0.28125,0.265625 0.3125,0 0.375,-0.25 0.453125,-0.5625 0.140625,-0.5625 0.515625,-2.015625 0.59375,-2.40625 0.03125,-0.125 0.5625,-1.328125 1.65625,-1.328125 0.421875,0 0.53125,0.34375 0.53125,0.703125 0,0.5625 -0.421875,1.703125 -0.625,2.234375 -0.078125,0.234375 -0.125,0.34375 -0.125,0.546875 0,0.46875 0.34375,0.8125 0.8125,0.8125 0.9375,0 1.3125,-1.453125 1.3125,-1.53125 0,-0.109375 -0.09375,-0.109375 -0.125,-0.109375 -0.09375,0 -0.09375,0.03125 -0.140625,0.1875 -0.15625,0.53125 -0.46875,1.234375 -1.015625,1.234375 -0.171875,0 -0.25,-0.09375 -0.25,-0.328125 0,-0.25 0.09375,-0.484375 0.1875,-0.703125 0.1875,-0.53125 0.609375,-1.625 0.609375,-2.203125 0,-0.640625 -0.40625,-1.0625 -1.15625,-1.0625 -0.734375,0 -1.25,0.4375 -1.625,0.96875 0,-0.125 -0.03125,-0.46875 -0.3125,-0.703125 -0.25,-0.21875 -0.5625,-0.265625 -0.8125,-0.265625 -0.90625,0 -1.390625,0.640625 -1.5625,0.875 -0.046875,-0.578125 -0.46875,-0.875 -0.921875,-0.875 -0.453125,0 -0.640625,0.390625 -0.734375,0.5625 -0.171875,0.359375 -0.296875,0.9375 -0.296875,0.96875 0,0.109375 0.09375,0.109375 0.109375,0.109375 0.109375,0 0.109375,-0.015625 0.171875,-0.234375 0.171875,-0.703125 0.375,-1.1875 0.734375,-1.1875 0.15625,0 0.296875,0.078125 0.296875,0.453125 0,0.21875 -0.03125,0.328125 -0.15625,0.84375 z" id="path6097" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-998f6c43-2" overflow="visible" style="overflow:visible">
               <path d="" id="path6100" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-998f6c43-3" overflow="visible" style="overflow:visible">
               <path d="M 3.59375,-2.21875 C 3.59375,-2.984375 3.5,-3.546875 3.1875,-4.03125 2.96875,-4.34375 2.53125,-4.625 1.984375,-4.625 c -1.625,0 -1.625,1.90625 -1.625,2.40625 0,0.5 0,2.359375 1.625,2.359375 1.609375,0 1.609375,-1.859375 1.609375,-2.359375 z M 1.984375,-0.0625 c -0.328125,0 -0.75,-0.1875 -0.890625,-0.75 C 1,-1.21875 1,-1.796875 1,-2.3125 1,-2.828125 1,-3.359375 1.09375,-3.734375 1.25,-4.28125 1.6875,-4.4375 1.984375,-4.4375 c 0.375,0 0.734375,0.234375 0.859375,0.640625 0.109375,0.375 0.125,0.875 0.125,1.484375 0,0.515625 0,1.03125 -0.09375,1.46875 -0.140625,0.640625 -0.609375,0.78125 -0.890625,0.78125 z" id="path6103" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
           </g>
         </defs>
         <g id="textext-998f6c43-4">
           <g id="g6106" style="fill:#000000;fill-opacity:1">
             <use height="360" id="use6108" width="360" x="223.43201" xlink:href="#textext-998f6c43-1" y="134.765"/>
           </g>
           <g id="g6110" style="fill:#000000;fill-opacity:1">
             <use height="360" id="use6112" width="360" x="232.179" xlink:href="#textext-998f6c43-3" y="136.259"/>
           </g>
         </g>
       </g>
       <g id="g6370" ns0:preamble="" ns0:text="$m_1$" transform="translate(-3.402887,815.69608)">
         <defs id="defs6372">
           <g id="g6374">
             <symbol id="textext-b1060afd-0" overflow="visible" style="overflow:visible">
               <path d="" id="path6377" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-b1060afd-1" overflow="visible" style="overflow:visible">
               <path d="m 0.875,-0.59375 c -0.03125,0.15625 -0.09375,0.390625 -0.09375,0.4375 0,0.171875 0.140625,0.265625 0.296875,0.265625 0.125,0 0.296875,-0.078125 0.375,-0.28125 0,-0.015625 0.125,-0.484375 0.1875,-0.734375 l 0.21875,-0.890625 C 1.90625,-2.03125 1.96875,-2.25 2.03125,-2.46875 c 0.03125,-0.171875 0.109375,-0.46875 0.125,-0.5 0.140625,-0.3125 0.671875,-1.21875 1.625,-1.21875 0.453125,0 0.53125,0.375 0.53125,0.703125 0,0.25 -0.0625,0.53125 -0.140625,0.828125 L 3.890625,-1.5 3.6875,-0.75 c -0.03125,0.203125 -0.125,0.546875 -0.125,0.59375 0,0.171875 0.140625,0.265625 0.28125,0.265625 0.3125,0 0.375,-0.25 0.453125,-0.5625 0.140625,-0.5625 0.515625,-2.015625 0.59375,-2.40625 0.03125,-0.125 0.5625,-1.328125 1.65625,-1.328125 0.421875,0 0.53125,0.34375 0.53125,0.703125 0,0.5625 -0.421875,1.703125 -0.625,2.234375 -0.078125,0.234375 -0.125,0.34375 -0.125,0.546875 0,0.46875 0.34375,0.8125 0.8125,0.8125 0.9375,0 1.3125,-1.453125 1.3125,-1.53125 0,-0.109375 -0.09375,-0.109375 -0.125,-0.109375 -0.09375,0 -0.09375,0.03125 -0.140625,0.1875 -0.15625,0.53125 -0.46875,1.234375 -1.015625,1.234375 -0.171875,0 -0.25,-0.09375 -0.25,-0.328125 0,-0.25 0.09375,-0.484375 0.1875,-0.703125 0.1875,-0.53125 0.609375,-1.625 0.609375,-2.203125 0,-0.640625 -0.40625,-1.0625 -1.15625,-1.0625 -0.734375,0 -1.25,0.4375 -1.625,0.96875 0,-0.125 -0.03125,-0.46875 -0.3125,-0.703125 -0.25,-0.21875 -0.5625,-0.265625 -0.8125,-0.265625 -0.90625,0 -1.390625,0.640625 -1.5625,0.875 -0.046875,-0.578125 -0.46875,-0.875 -0.921875,-0.875 -0.453125,0 -0.640625,0.390625 -0.734375,0.5625 -0.171875,0.359375 -0.296875,0.9375 -0.296875,0.96875 0,0.109375 0.09375,0.109375 0.109375,0.109375 0.109375,0 0.109375,-0.015625 0.171875,-0.234375 0.171875,-0.703125 0.375,-1.1875 0.734375,-1.1875 0.15625,0 0.296875,0.078125 0.296875,0.453125 0,0.21875 -0.03125,0.328125 -0.15625,0.84375 z" id="path6380" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-b1060afd-2" overflow="visible" style="overflow:visible">
               <path d="" id="path6383" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-b1060afd-3" overflow="visible" style="overflow:visible">
               <path d="m 2.328125,-4.4375 c 0,-0.1875 0,-0.1875 -0.203125,-0.1875 -0.453125,0.4375 -1.078125,0.4375 -1.359375,0.4375 l 0,0.25 c 0.15625,0 0.625,0 1,-0.1875 l 0,3.546875 c 0,0.234375 0,0.328125 -0.6875,0.328125 l -0.265625,0 0,0.25 c 0.125,0 0.984375,-0.03125 1.234375,-0.03125 0.21875,0 1.09375,0.03125 1.25,0.03125 l 0,-0.25 -0.265625,0 c -0.703125,0 -0.703125,-0.09375 -0.703125,-0.328125 z" id="path6386" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
           </g>
         </defs>
         <g id="textext-b1060afd-4">
           <g id="g6389" style="fill:#000000;fill-opacity:1">
             <use height="360" id="use6391" width="360" x="223.43201" xlink:href="#textext-b1060afd-1" y="134.765"/>
           </g>
           <g id="g6393" style="fill:#000000;fill-opacity:1">
             <use height="360" id="use6395" width="360" x="232.179" xlink:href="#textext-b1060afd-3" y="136.259"/>
           </g>
         </g>
       </g>
       <g id="g6685" ns0:preamble="" ns0:text="$m_{n+1}$" transform="translate(56.490918,671.0589)">
         <defs id="defs6687">
           <g id="g6689">
             <symbol id="textext-a452b3d5-0" overflow="visible" style="overflow:visible">
               <path d="" id="path6692" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-a452b3d5-1" overflow="visible" style="overflow:visible">
               <path d="m 0.875,-0.59375 c -0.03125,0.15625 -0.09375,0.390625 -0.09375,0.4375 0,0.171875 0.140625,0.265625 0.296875,0.265625 0.125,0 0.296875,-0.078125 0.375,-0.28125 0,-0.015625 0.125,-0.484375 0.1875,-0.734375 l 0.21875,-0.890625 C 1.90625,-2.03125 1.96875,-2.25 2.03125,-2.46875 c 0.03125,-0.171875 0.109375,-0.46875 0.125,-0.5 0.140625,-0.3125 0.671875,-1.21875 1.625,-1.21875 0.453125,0 0.53125,0.375 0.53125,0.703125 0,0.25 -0.0625,0.53125 -0.140625,0.828125 L 3.890625,-1.5 3.6875,-0.75 c -0.03125,0.203125 -0.125,0.546875 -0.125,0.59375 0,0.171875 0.140625,0.265625 0.28125,0.265625 0.3125,0 0.375,-0.25 0.453125,-0.5625 0.140625,-0.5625 0.515625,-2.015625 0.59375,-2.40625 0.03125,-0.125 0.5625,-1.328125 1.65625,-1.328125 0.421875,0 0.53125,0.34375 0.53125,0.703125 0,0.5625 -0.421875,1.703125 -0.625,2.234375 -0.078125,0.234375 -0.125,0.34375 -0.125,0.546875 0,0.46875 0.34375,0.8125 0.8125,0.8125 0.9375,0 1.3125,-1.453125 1.3125,-1.53125 0,-0.109375 -0.09375,-0.109375 -0.125,-0.109375 -0.09375,0 -0.09375,0.03125 -0.140625,0.1875 -0.15625,0.53125 -0.46875,1.234375 -1.015625,1.234375 -0.171875,0 -0.25,-0.09375 -0.25,-0.328125 0,-0.25 0.09375,-0.484375 0.1875,-0.703125 0.1875,-0.53125 0.609375,-1.625 0.609375,-2.203125 0,-0.640625 -0.40625,-1.0625 -1.15625,-1.0625 -0.734375,0 -1.25,0.4375 -1.625,0.96875 0,-0.125 -0.03125,-0.46875 -0.3125,-0.703125 -0.25,-0.21875 -0.5625,-0.265625 -0.8125,-0.265625 -0.90625,0 -1.390625,0.640625 -1.5625,0.875 -0.046875,-0.578125 -0.46875,-0.875 -0.921875,-0.875 -0.453125,0 -0.640625,0.390625 -0.734375,0.5625 -0.171875,0.359375 -0.296875,0.9375 -0.296875,0.96875 0,0.109375 0.09375,0.109375 0.109375,0.109375 0.109375,0 0.109375,-0.015625 0.171875,-0.234375 0.171875,-0.703125 0.375,-1.1875 0.734375,-1.1875 0.15625,0 0.296875,0.078125 0.296875,0.453125 0,0.21875 -0.03125,0.328125 -0.15625,0.84375 z" id="path6695" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-a452b3d5-2" overflow="visible" style="overflow:visible">
               <path d="" id="path6698" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-a452b3d5-3" overflow="visible" style="overflow:visible">
               <path d="m 0.84375,-0.4375 c -0.015625,0.09375 -0.0625,0.265625 -0.0625,0.28125 0,0.15625 0.125,0.21875 0.234375,0.21875 0.125,0 0.234375,-0.078125 0.28125,-0.140625 0.03125,-0.0625 0.078125,-0.296875 0.125,-0.4375 0.03125,-0.125 0.109375,-0.453125 0.140625,-0.625 0.046875,-0.15625 0.09375,-0.3125 0.125,-0.46875 0.078125,-0.28125 0.09375,-0.34375 0.296875,-0.625 C 2.171875,-2.515625 2.5,-2.875 3.03125,-2.875 c 0.390625,0 0.40625,0.359375 0.40625,0.484375 0,0.421875 -0.296875,1.1875 -0.40625,1.484375 -0.078125,0.203125 -0.109375,0.265625 -0.109375,0.375 0,0.375 0.296875,0.59375 0.65625,0.59375 0.703125,0 1,-0.953125 1,-1.0625 0,-0.09375 -0.078125,-0.09375 -0.109375,-0.09375 -0.09375,0 -0.09375,0.046875 -0.125,0.125 C 4.1875,-0.40625 3.875,-0.125 3.609375,-0.125 c -0.15625,0 -0.1875,-0.09375 -0.1875,-0.25 0,-0.15625 0.046875,-0.25 0.171875,-0.5625 0.078125,-0.21875 0.359375,-0.953125 0.359375,-1.34375 0,-0.671875 -0.53125,-0.796875 -0.90625,-0.796875 -0.578125,0 -0.96875,0.359375 -1.171875,0.640625 -0.046875,-0.484375 -0.453125,-0.640625 -0.75,-0.640625 -0.296875,0 -0.453125,0.21875 -0.546875,0.375 -0.15625,0.265625 -0.25,0.65625 -0.25,0.703125 0,0.078125 0.09375,0.078125 0.125,0.078125 0.09375,0 0.09375,-0.015625 0.140625,-0.203125 0.109375,-0.40625 0.25,-0.75 0.515625,-0.75 0.1875,0 0.234375,0.15625 0.234375,0.34375 0,0.125 -0.0625,0.390625 -0.125,0.578125 -0.046875,0.1875 -0.109375,0.46875 -0.140625,0.625 z" id="path6701" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-a452b3d5-4" overflow="visible" style="overflow:visible">
               <path d="" id="path6704" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-a452b3d5-5" overflow="visible" style="overflow:visible">
               <path d="m 3.21875,-1.578125 2.140625,0 c 0.09375,0 0.25,0 0.25,-0.15625 0,-0.1875 -0.15625,-0.1875 -0.25,-0.1875 l -2.140625,0 0,-2.140625 c 0,-0.078125 0,-0.25 -0.15625,-0.25 -0.171875,0 -0.171875,0.15625 -0.171875,0.25 l 0,2.140625 -2.140625,0 c -0.09375,0 -0.265625,0 -0.265625,0.171875 0,0.171875 0.15625,0.171875 0.265625,0.171875 l 2.140625,0 0,2.140625 c 0,0.09375 0,0.265625 0.15625,0.265625 0.171875,0 0.171875,-0.171875 0.171875,-0.265625 z" id="path6707" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-a452b3d5-6" overflow="visible" style="overflow:visible">
               <path d="m 2.328125,-4.4375 c 0,-0.1875 0,-0.1875 -0.203125,-0.1875 -0.453125,0.4375 -1.078125,0.4375 -1.359375,0.4375 l 0,0.25 c 0.15625,0 0.625,0 1,-0.1875 l 0,3.546875 c 0,0.234375 0,0.328125 -0.6875,0.328125 l -0.265625,0 0,0.25 c 0.125,0 0.984375,-0.03125 1.234375,-0.03125 0.21875,0 1.09375,0.03125 1.25,0.03125 l 0,-0.25 -0.265625,0 c -0.703125,0 -0.703125,-0.09375 -0.703125,-0.328125 z" id="path6710" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
           </g>
         </defs>
         <g id="textext-a452b3d5-7">
           <g id="g6713" style="fill:#000000;fill-opacity:1">
             <use height="360" id="use6715" width="360" x="223.43201" xlink:href="#textext-a452b3d5-1" y="134.765"/>
           </g>
           <g id="g6717" style="fill:#000000;fill-opacity:1">
             <use height="360" id="use6719" width="360" x="232.179" xlink:href="#textext-a452b3d5-3" y="136.259"/>
           </g>
           <g id="g6721" style="fill:#000000;fill-opacity:1">
             <use height="360" id="use6723" width="360" x="237.104" xlink:href="#textext-a452b3d5-5" y="136.259"/>
             <use height="360" id="use6725" width="360" x="243.22002" xlink:href="#textext-a452b3d5-6" y="136.259"/>
           </g>
         </g>
       </g>
       <g id="g7065" ns0:preamble="" ns0:text="$m_n$" transform="translate(48.8449,755.1651)">
         <defs id="defs7067">
           <g id="g7069">
             <symbol id="textext-c4d0d8e4-0" overflow="visible" style="overflow:visible">
               <path d="" id="path7072" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-c4d0d8e4-1" overflow="visible" style="overflow:visible">
               <path d="m 0.875,-0.59375 c -0.03125,0.15625 -0.09375,0.390625 -0.09375,0.4375 0,0.171875 0.140625,0.265625 0.296875,0.265625 0.125,0 0.296875,-0.078125 0.375,-0.28125 0,-0.015625 0.125,-0.484375 0.1875,-0.734375 l 0.21875,-0.890625 C 1.90625,-2.03125 1.96875,-2.25 2.03125,-2.46875 c 0.03125,-0.171875 0.109375,-0.46875 0.125,-0.5 0.140625,-0.3125 0.671875,-1.21875 1.625,-1.21875 0.453125,0 0.53125,0.375 0.53125,0.703125 0,0.25 -0.0625,0.53125 -0.140625,0.828125 L 3.890625,-1.5 3.6875,-0.75 c -0.03125,0.203125 -0.125,0.546875 -0.125,0.59375 0,0.171875 0.140625,0.265625 0.28125,0.265625 0.3125,0 0.375,-0.25 0.453125,-0.5625 0.140625,-0.5625 0.515625,-2.015625 0.59375,-2.40625 0.03125,-0.125 0.5625,-1.328125 1.65625,-1.328125 0.421875,0 0.53125,0.34375 0.53125,0.703125 0,0.5625 -0.421875,1.703125 -0.625,2.234375 -0.078125,0.234375 -0.125,0.34375 -0.125,0.546875 0,0.46875 0.34375,0.8125 0.8125,0.8125 0.9375,0 1.3125,-1.453125 1.3125,-1.53125 0,-0.109375 -0.09375,-0.109375 -0.125,-0.109375 -0.09375,0 -0.09375,0.03125 -0.140625,0.1875 -0.15625,0.53125 -0.46875,1.234375 -1.015625,1.234375 -0.171875,0 -0.25,-0.09375 -0.25,-0.328125 0,-0.25 0.09375,-0.484375 0.1875,-0.703125 0.1875,-0.53125 0.609375,-1.625 0.609375,-2.203125 0,-0.640625 -0.40625,-1.0625 -1.15625,-1.0625 -0.734375,0 -1.25,0.4375 -1.625,0.96875 0,-0.125 -0.03125,-0.46875 -0.3125,-0.703125 -0.25,-0.21875 -0.5625,-0.265625 -0.8125,-0.265625 -0.90625,0 -1.390625,0.640625 -1.5625,0.875 -0.046875,-0.578125 -0.46875,-0.875 -0.921875,-0.875 -0.453125,0 -0.640625,0.390625 -0.734375,0.5625 -0.171875,0.359375 -0.296875,0.9375 -0.296875,0.96875 0,0.109375 0.09375,0.109375 0.109375,0.109375 0.109375,0 0.109375,-0.015625 0.171875,-0.234375 0.171875,-0.703125 0.375,-1.1875 0.734375,-1.1875 0.15625,0 0.296875,0.078125 0.296875,0.453125 0,0.21875 -0.03125,0.328125 -0.15625,0.84375 z" id="path7075" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-c4d0d8e4-2" overflow="visible" style="overflow:visible">
               <path d="" id="path7078" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-c4d0d8e4-3" overflow="visible" style="overflow:visible">
               <path d="m 0.84375,-0.4375 c -0.015625,0.09375 -0.0625,0.265625 -0.0625,0.28125 0,0.15625 0.125,0.21875 0.234375,0.21875 0.125,0 0.234375,-0.078125 0.28125,-0.140625 0.03125,-0.0625 0.078125,-0.296875 0.125,-0.4375 0.03125,-0.125 0.109375,-0.453125 0.140625,-0.625 0.046875,-0.15625 0.09375,-0.3125 0.125,-0.46875 0.078125,-0.28125 0.09375,-0.34375 0.296875,-0.625 C 2.171875,-2.515625 2.5,-2.875 3.03125,-2.875 c 0.390625,0 0.40625,0.359375 0.40625,0.484375 0,0.421875 -0.296875,1.1875 -0.40625,1.484375 -0.078125,0.203125 -0.109375,0.265625 -0.109375,0.375 0,0.375 0.296875,0.59375 0.65625,0.59375 0.703125,0 1,-0.953125 1,-1.0625 0,-0.09375 -0.078125,-0.09375 -0.109375,-0.09375 -0.09375,0 -0.09375,0.046875 -0.125,0.125 C 4.1875,-0.40625 3.875,-0.125 3.609375,-0.125 c -0.15625,0 -0.1875,-0.09375 -0.1875,-0.25 0,-0.15625 0.046875,-0.25 0.171875,-0.5625 0.078125,-0.21875 0.359375,-0.953125 0.359375,-1.34375 0,-0.671875 -0.53125,-0.796875 -0.90625,-0.796875 -0.578125,0 -0.96875,0.359375 -1.171875,0.640625 -0.046875,-0.484375 -0.453125,-0.640625 -0.75,-0.640625 -0.296875,0 -0.453125,0.21875 -0.546875,0.375 -0.15625,0.265625 -0.25,0.65625 -0.25,0.703125 0,0.078125 0.09375,0.078125 0.125,0.078125 0.09375,0 0.09375,-0.015625 0.140625,-0.203125 0.109375,-0.40625 0.25,-0.75 0.515625,-0.75 0.1875,0 0.234375,0.15625 0.234375,0.34375 0,0.125 -0.0625,0.390625 -0.125,0.578125 -0.046875,0.1875 -0.109375,0.46875 -0.140625,0.625 z" id="path7081" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
           </g>
         </defs>
         <g id="textext-c4d0d8e4-4">
           <g id="g7084" style="fill:#000000;fill-opacity:1">
             <use height="360" id="use7086" width="360" x="223.43201" xlink:href="#textext-c4d0d8e4-1" y="134.765"/>
           </g>
           <g id="g7088" style="fill:#000000;fill-opacity:1">
             <use height="360" id="use7090" width="360" x="232.179" xlink:href="#textext-c4d0d8e4-3" y="136.259"/>
           </g>
         </g>
       </g>
       <path d="m 39.504425,1008.7314 0,28.6726" id="path7276" inkscape:connector-curvature="0" style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"/>
       <path d="m 167.8938,1016.7491 0,20.2508" id="path7276-2" inkscape:connector-curvature="0" sodipodi:nodetypes="cc" style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"/>
       <path d="m 39.504425,1032.289 54.639111,0" id="path7296" inkscape:connector-curvature="0" sodipodi:nodetypes="cc" style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1;marker-start:none"/>
       <path d="m 112.74623,1032.2889 53.06221,0" id="path7298" inkscape:connector-curvature="0" sodipodi:nodetypes="cc" style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1;marker-end:url(#Arrow1Send)"/>
       <g id="g8966" ns0:preamble="" ns0:text="$\\hat{i}_x$" transform="translate(-133.30401,880.3294)">
         <defs id="defs8968">
           <g id="g8970">
             <symbol id="textext-77f6b85a-0" overflow="visible" style="overflow:visible">
               <path d="" id="path8973" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-77f6b85a-1" overflow="visible" style="overflow:visible">
               <path d="M 2.5,-6.921875 1.15625,-5.5625 1.328125,-5.390625 2.5,-6.40625 3.640625,-5.390625 3.8125,-5.5625 z" id="path8976" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-77f6b85a-2" overflow="visible" style="overflow:visible">
               <path d="" id="path8979" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-77f6b85a-3" overflow="visible" style="overflow:visible">
               <path d="m 2.828125,-6.234375 c 0,-0.203125 -0.140625,-0.359375 -0.359375,-0.359375 -0.28125,0 -0.546875,0.265625 -0.546875,0.53125 0,0.1875 0.140625,0.359375 0.375,0.359375 0.234375,0 0.53125,-0.234375 0.53125,-0.53125 z m -0.75,3.75 c 0.109375,-0.28125 0.109375,-0.3125 0.21875,-0.578125 0.078125,-0.203125 0.125,-0.34375 0.125,-0.53125 0,-0.4375 -0.3125,-0.8125 -0.8125,-0.8125 -0.9375,0 -1.3125,1.453125 -1.3125,1.53125 0,0.109375 0.09375,0.109375 0.109375,0.109375 0.109375,0 0.109375,-0.03125 0.15625,-0.1875 0.28125,-0.9375 0.671875,-1.234375 1.015625,-1.234375 0.078125,0 0.25,0 0.25,0.3125 0,0.21875 -0.078125,0.421875 -0.109375,0.53125 -0.078125,0.25 -0.53125,1.40625 -0.6875,1.84375 -0.109375,0.25 -0.234375,0.578125 -0.234375,0.796875 0,0.46875 0.34375,0.8125 0.8125,0.8125 0.9375,0 1.3125,-1.4375 1.3125,-1.53125 0,-0.109375 -0.09375,-0.109375 -0.125,-0.109375 -0.09375,0 -0.09375,0.03125 -0.140625,0.1875 -0.1875,0.625 -0.515625,1.234375 -1.015625,1.234375 -0.171875,0 -0.25,-0.09375 -0.25,-0.328125 0,-0.25 0.0625,-0.390625 0.296875,-1 z" id="path8982" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-77f6b85a-4" overflow="visible" style="overflow:visible">
               <path d="" id="path8985" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-77f6b85a-5" overflow="visible" style="overflow:visible">
               <path d="M 1.734375,-0.734375 C 1.671875,-0.5 1.4375,-0.125 1.078125,-0.125 c -0.015625,0 -0.234375,0 -0.375,-0.09375 0.28125,-0.09375 0.3125,-0.34375 0.3125,-0.390625 0,-0.15625 -0.125,-0.25 -0.28125,-0.25 -0.203125,0 -0.40625,0.15625 -0.40625,0.421875 0,0.34375 0.390625,0.5 0.734375,0.5 0.328125,0 0.609375,-0.1875 0.78125,-0.484375 C 2.015625,-0.0625 2.390625,0.0625 2.671875,0.0625 c 0.8125,0 1.234375,-0.859375 1.234375,-1.0625 0,-0.09375 -0.09375,-0.09375 -0.109375,-0.09375 -0.109375,0 -0.109375,0.046875 -0.140625,0.125 -0.140625,0.484375 -0.5625,0.84375 -0.953125,0.84375 -0.28125,0 -0.421875,-0.1875 -0.421875,-0.453125 0,-0.1875 0.171875,-0.8125 0.359375,-1.59375 C 2.78125,-2.703125 3.09375,-2.875 3.328125,-2.875 c 0.015625,0 0.21875,0 0.375,0.09375 -0.21875,0.0625 -0.3125,0.265625 -0.3125,0.390625 0,0.140625 0.125,0.25 0.28125,0.25 0.15625,0 0.390625,-0.125 0.390625,-0.421875 0,-0.390625 -0.453125,-0.515625 -0.71875,-0.515625 -0.359375,0 -0.640625,0.234375 -0.78125,0.5 -0.125,-0.28125 -0.453125,-0.5 -0.84375,-0.5 C 0.9375,-3.078125 0.5,-2.21875 0.5,-2 c 0,0.078125 0.09375,0.078125 0.109375,0.078125 0.09375,0 0.09375,-0.015625 0.140625,-0.109375 C 0.921875,-2.578125 1.359375,-2.875 1.703125,-2.875 1.9375,-2.875 2.125,-2.75 2.125,-2.421875 2.125,-2.28125 2.03125,-1.9375 1.96875,-1.6875 z" id="path8988" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
           </g>
         </defs>
         <g id="textext-77f6b85a-6">
           <g id="g8991" style="fill:#000000;fill-opacity:1">
             <use height="360" id="use8993" width="360" x="222.658" xlink:href="#textext-77f6b85a-1" y="132.483"/>
           </g>
           <g id="g8995" style="fill:#000000;fill-opacity:1">
             <use height="360" id="use8997" width="360" x="223.43201" xlink:href="#textext-77f6b85a-3" y="134.765"/>
           </g>
           <g id="g8999" style="fill:#000000;fill-opacity:1">
             <use height="360" id="use9001" width="360" x="226.864" xlink:href="#textext-77f6b85a-5" y="136.259"/>
           </g>
         </g>
       </g>
       <g id="g9445" ns0:preamble="" ns0:text="$\\hat{i}_y$" transform="translate(-196.38366,815.97542)">
         <defs id="defs9447">
           <g id="g9449">
             <symbol id="textext-9fe1e674-0" overflow="visible" style="overflow:visible">
               <path d="" id="path9452" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-9fe1e674-1" overflow="visible" style="overflow:visible">
               <path d="M 2.5,-6.921875 1.15625,-5.5625 1.328125,-5.390625 2.5,-6.40625 3.640625,-5.390625 3.8125,-5.5625 z" id="path9455" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-9fe1e674-2" overflow="visible" style="overflow:visible">
               <path d="" id="path9458" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-9fe1e674-3" overflow="visible" style="overflow:visible">
               <path d="m 2.828125,-6.234375 c 0,-0.203125 -0.140625,-0.359375 -0.359375,-0.359375 -0.28125,0 -0.546875,0.265625 -0.546875,0.53125 0,0.1875 0.140625,0.359375 0.375,0.359375 0.234375,0 0.53125,-0.234375 0.53125,-0.53125 z m -0.75,3.75 c 0.109375,-0.28125 0.109375,-0.3125 0.21875,-0.578125 0.078125,-0.203125 0.125,-0.34375 0.125,-0.53125 0,-0.4375 -0.3125,-0.8125 -0.8125,-0.8125 -0.9375,0 -1.3125,1.453125 -1.3125,1.53125 0,0.109375 0.09375,0.109375 0.109375,0.109375 0.109375,0 0.109375,-0.03125 0.15625,-0.1875 0.28125,-0.9375 0.671875,-1.234375 1.015625,-1.234375 0.078125,0 0.25,0 0.25,0.3125 0,0.21875 -0.078125,0.421875 -0.109375,0.53125 -0.078125,0.25 -0.53125,1.40625 -0.6875,1.84375 -0.109375,0.25 -0.234375,0.578125 -0.234375,0.796875 0,0.46875 0.34375,0.8125 0.8125,0.8125 0.9375,0 1.3125,-1.4375 1.3125,-1.53125 0,-0.109375 -0.09375,-0.109375 -0.125,-0.109375 -0.09375,0 -0.09375,0.03125 -0.140625,0.1875 -0.1875,0.625 -0.515625,1.234375 -1.015625,1.234375 -0.171875,0 -0.25,-0.09375 -0.25,-0.328125 0,-0.25 0.0625,-0.390625 0.296875,-1 z" id="path9461" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-9fe1e674-4" overflow="visible" style="overflow:visible">
               <path d="" id="path9464" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-9fe1e674-5" overflow="visible" style="overflow:visible">
               <path d="M 3.875,-2.625 C 3.90625,-2.71875 3.90625,-2.734375 3.90625,-2.78125 3.90625,-2.921875 3.796875,-3 3.671875,-3 3.59375,-3 3.46875,-2.96875 3.390625,-2.84375 3.359375,-2.796875 3.3125,-2.578125 3.28125,-2.4375 L 3.125,-1.859375 c -0.03125,0.171875 -0.25,1.046875 -0.28125,1.125 0,0 -0.3125,0.609375 -0.84375,0.609375 -0.484375,0 -0.484375,-0.453125 -0.484375,-0.578125 0,-0.375 0.15625,-0.8125 0.375,-1.359375 C 1.96875,-2.28125 2,-2.359375 2,-2.484375 2,-2.8125 1.71875,-3.078125 1.34375,-3.078125 0.640625,-3.078125 0.328125,-2.125 0.328125,-2 c 0,0.078125 0.09375,0.078125 0.125,0.078125 0.09375,0 0.09375,-0.03125 0.125,-0.109375 C 0.75,-2.609375 1.046875,-2.875 1.328125,-2.875 1.4375,-2.875 1.5,-2.796875 1.5,-2.640625 c 0,0.171875 -0.0625,0.3125 -0.09375,0.40625 C 1.0625,-1.375 1,-1.125 1,-0.8125 1,-0.703125 1,-0.375 1.265625,-0.140625 1.484375,0.03125 1.78125,0.0625 1.96875,0.0625 2.25,0.0625 2.5,-0.03125 2.71875,-0.25 2.640625,0.140625 2.5625,0.4375 2.265625,0.78125 2.078125,1 1.796875,1.21875 1.421875,1.21875 c -0.046875,0 -0.375,0 -0.515625,-0.21875 0.375,-0.046875 0.375,-0.375 0.375,-0.390625 0,-0.21875 -0.203125,-0.265625 -0.265625,-0.265625 -0.171875,0 -0.40625,0.140625 -0.40625,0.46875 0,0.34375 0.328125,0.609375 0.828125,0.609375 C 2.140625,1.421875 3,0.875 3.21875,0 z" id="path9467" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
           </g>
         </defs>
         <g id="textext-9fe1e674-6">
           <g id="g9470" style="fill:#000000;fill-opacity:1">
             <use height="360" id="use9472" width="360" x="222.658" xlink:href="#textext-9fe1e674-1" y="132.483"/>
           </g>
           <g id="g9474" style="fill:#000000;fill-opacity:1">
             <use height="360" id="use9476" width="360" x="223.43201" xlink:href="#textext-9fe1e674-3" y="134.765"/>
           </g>
           <g id="g9478" style="fill:#000000;fill-opacity:1">
             <use height="360" id="use9480" width="360" x="226.864" xlink:href="#textext-9fe1e674-5" y="136.259"/>
           </g>
         </g>
       </g>
       <g id="g10006" ns0:preamble="" ns0:text="$l_0$" transform="translate(-29.77207,838.3967)">
         <defs id="defs10008">
           <g id="g10010">
             <symbol id="textext-03c909df-0" overflow="visible" style="overflow:visible">
               <path d="" id="path10013" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-03c909df-1" overflow="visible" style="overflow:visible">
               <path d="m 2.578125,-6.8125 c 0,0 0,-0.109375 -0.140625,-0.109375 -0.21875,0 -0.953125,0.078125 -1.21875,0.109375 -0.078125,0 -0.1875,0.015625 -0.1875,0.203125 0,0.109375 0.109375,0.109375 0.25,0.109375 0.484375,0 0.5,0.09375 0.5,0.171875 L 1.75,-6.125 0.484375,-1.140625 C 0.453125,-1.03125 0.4375,-0.96875 0.4375,-0.8125 c 0,0.578125 0.4375,0.921875 0.90625,0.921875 0.328125,0 0.578125,-0.203125 0.75,-0.5625 0.171875,-0.375 0.296875,-0.953125 0.296875,-0.96875 0,-0.109375 -0.09375,-0.109375 -0.125,-0.109375 -0.09375,0 -0.109375,0.046875 -0.125,0.1875 C 1.96875,-0.703125 1.78125,-0.109375 1.375,-0.109375 c -0.296875,0 -0.296875,-0.3125 -0.296875,-0.453125 0,-0.25 0.015625,-0.296875 0.0625,-0.484375 z" id="path10016" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-03c909df-2" overflow="visible" style="overflow:visible">
               <path d="" id="path10019" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-03c909df-3" overflow="visible" style="overflow:visible">
               <path d="M 3.59375,-2.21875 C 3.59375,-2.984375 3.5,-3.546875 3.1875,-4.03125 2.96875,-4.34375 2.53125,-4.625 1.984375,-4.625 c -1.625,0 -1.625,1.90625 -1.625,2.40625 0,0.5 0,2.359375 1.625,2.359375 1.609375,0 1.609375,-1.859375 1.609375,-2.359375 z M 1.984375,-0.0625 c -0.328125,0 -0.75,-0.1875 -0.890625,-0.75 C 1,-1.21875 1,-1.796875 1,-2.3125 1,-2.828125 1,-3.359375 1.09375,-3.734375 1.25,-4.28125 1.6875,-4.4375 1.984375,-4.4375 c 0.375,0 0.734375,0.234375 0.859375,0.640625 0.109375,0.375 0.125,0.875 0.125,1.484375 0,0.515625 0,1.03125 -0.09375,1.46875 -0.140625,0.640625 -0.609375,0.78125 -0.890625,0.78125 z" id="path10022" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
           </g>
         </defs>
         <g id="textext-03c909df-4">
           <g id="g10025" style="fill:#000000;fill-opacity:1">
             <use height="360" id="use10027" width="360" x="223.43201" xlink:href="#textext-03c909df-1" y="134.765"/>
           </g>
           <g id="g10029" style="fill:#000000;fill-opacity:1">
             <use height="360" id="use10031" width="360" x="226.405" xlink:href="#textext-03c909df-3" y="136.259"/>
           </g>
         </g>
       </g>
       <g id="g10535" ns0:preamble="" ns0:text="$l_1$" transform="translate(30.121736,785.51174)">
         <defs id="defs10537">
           <g id="g10539">
             <symbol id="textext-76adb4f4-0" overflow="visible" style="overflow:visible">
               <path d="" id="path10542" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-76adb4f4-1" overflow="visible" style="overflow:visible">
               <path d="m 2.578125,-6.8125 c 0,0 0,-0.109375 -0.140625,-0.109375 -0.21875,0 -0.953125,0.078125 -1.21875,0.109375 -0.078125,0 -0.1875,0.015625 -0.1875,0.203125 0,0.109375 0.109375,0.109375 0.25,0.109375 0.484375,0 0.5,0.09375 0.5,0.171875 L 1.75,-6.125 0.484375,-1.140625 C 0.453125,-1.03125 0.4375,-0.96875 0.4375,-0.8125 c 0,0.578125 0.4375,0.921875 0.90625,0.921875 0.328125,0 0.578125,-0.203125 0.75,-0.5625 0.171875,-0.375 0.296875,-0.953125 0.296875,-0.96875 0,-0.109375 -0.09375,-0.109375 -0.125,-0.109375 -0.09375,0 -0.109375,0.046875 -0.125,0.1875 C 1.96875,-0.703125 1.78125,-0.109375 1.375,-0.109375 c -0.296875,0 -0.296875,-0.3125 -0.296875,-0.453125 0,-0.25 0.015625,-0.296875 0.0625,-0.484375 z" id="path10545" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-76adb4f4-2" overflow="visible" style="overflow:visible">
               <path d="" id="path10548" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-76adb4f4-3" overflow="visible" style="overflow:visible">
               <path d="m 2.328125,-4.4375 c 0,-0.1875 0,-0.1875 -0.203125,-0.1875 -0.453125,0.4375 -1.078125,0.4375 -1.359375,0.4375 l 0,0.25 c 0.15625,0 0.625,0 1,-0.1875 l 0,3.546875 c 0,0.234375 0,0.328125 -0.6875,0.328125 l -0.265625,0 0,0.25 c 0.125,0 0.984375,-0.03125 1.234375,-0.03125 0.21875,0 1.09375,0.03125 1.25,0.03125 l 0,-0.25 -0.265625,0 c -0.703125,0 -0.703125,-0.09375 -0.703125,-0.328125 z" id="path10551" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
           </g>
         </defs>
         <g id="textext-76adb4f4-4">
           <g id="g10554" style="fill:#000000;fill-opacity:1">
             <use height="360" id="use10556" width="360" x="223.43201" xlink:href="#textext-76adb4f4-1" y="134.765"/>
           </g>
           <g id="g10558" style="fill:#000000;fill-opacity:1">
             <use height="360" id="use10560" width="360" x="226.405" xlink:href="#textext-76adb4f4-3" y="136.259"/>
           </g>
         </g>
       </g>
       <g id="g11096" ns0:preamble="" ns0:text="$l_n$" transform="translate(65.165983,714.14892)">
         <defs id="defs11098">
           <g id="g11100">
             <symbol id="textext-a3e54763-0" overflow="visible" style="overflow:visible">
               <path d="" id="path11103" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-a3e54763-1" overflow="visible" style="overflow:visible">
               <path d="m 2.578125,-6.8125 c 0,0 0,-0.109375 -0.140625,-0.109375 -0.21875,0 -0.953125,0.078125 -1.21875,0.109375 -0.078125,0 -0.1875,0.015625 -0.1875,0.203125 0,0.109375 0.109375,0.109375 0.25,0.109375 0.484375,0 0.5,0.09375 0.5,0.171875 L 1.75,-6.125 0.484375,-1.140625 C 0.453125,-1.03125 0.4375,-0.96875 0.4375,-0.8125 c 0,0.578125 0.4375,0.921875 0.90625,0.921875 0.328125,0 0.578125,-0.203125 0.75,-0.5625 0.171875,-0.375 0.296875,-0.953125 0.296875,-0.96875 0,-0.109375 -0.09375,-0.109375 -0.125,-0.109375 -0.09375,0 -0.109375,0.046875 -0.125,0.1875 C 1.96875,-0.703125 1.78125,-0.109375 1.375,-0.109375 c -0.296875,0 -0.296875,-0.3125 -0.296875,-0.453125 0,-0.25 0.015625,-0.296875 0.0625,-0.484375 z" id="path11106" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-a3e54763-2" overflow="visible" style="overflow:visible">
               <path d="" id="path11109" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
             <symbol id="textext-a3e54763-3" overflow="visible" style="overflow:visible">
               <path d="m 0.84375,-0.4375 c -0.015625,0.09375 -0.0625,0.265625 -0.0625,0.28125 0,0.15625 0.125,0.21875 0.234375,0.21875 0.125,0 0.234375,-0.078125 0.28125,-0.140625 0.03125,-0.0625 0.078125,-0.296875 0.125,-0.4375 0.03125,-0.125 0.109375,-0.453125 0.140625,-0.625 0.046875,-0.15625 0.09375,-0.3125 0.125,-0.46875 0.078125,-0.28125 0.09375,-0.34375 0.296875,-0.625 C 2.171875,-2.515625 2.5,-2.875 3.03125,-2.875 c 0.390625,0 0.40625,0.359375 0.40625,0.484375 0,0.421875 -0.296875,1.1875 -0.40625,1.484375 -0.078125,0.203125 -0.109375,0.265625 -0.109375,0.375 0,0.375 0.296875,0.59375 0.65625,0.59375 0.703125,0 1,-0.953125 1,-1.0625 0,-0.09375 -0.078125,-0.09375 -0.109375,-0.09375 -0.09375,0 -0.09375,0.046875 -0.125,0.125 C 4.1875,-0.40625 3.875,-0.125 3.609375,-0.125 c -0.15625,0 -0.1875,-0.09375 -0.1875,-0.25 0,-0.15625 0.046875,-0.25 0.171875,-0.5625 0.078125,-0.21875 0.359375,-0.953125 0.359375,-1.34375 0,-0.671875 -0.53125,-0.796875 -0.90625,-0.796875 -0.578125,0 -0.96875,0.359375 -1.171875,0.640625 -0.046875,-0.484375 -0.453125,-0.640625 -0.75,-0.640625 -0.296875,0 -0.453125,0.21875 -0.546875,0.375 -0.15625,0.265625 -0.25,0.65625 -0.25,0.703125 0,0.078125 0.09375,0.078125 0.125,0.078125 0.09375,0 0.09375,-0.015625 0.140625,-0.203125 0.109375,-0.40625 0.25,-0.75 0.515625,-0.75 0.1875,0 0.234375,0.15625 0.234375,0.34375 0,0.125 -0.0625,0.390625 -0.125,0.578125 -0.046875,0.1875 -0.109375,0.46875 -0.140625,0.625 z" id="path11112" inkscape:connector-curvature="0" style="stroke:none"/>
             </symbol>
           </g>
         </defs>
         <g id="textext-a3e54763-4">
           <g id="g11115" style="fill:#000000;fill-opacity:1">
             <use height="360" id="use11117" width="360" x="223.43201" xlink:href="#textext-a3e54763-1" y="134.765"/>
           </g>
           <g id="g11119" style="fill:#000000;fill-opacity:1">
             <use height="360" id="use11121" width="360" x="226.405" xlink:href="#textext-a3e54763-3" y="136.259"/>
           </g>
         </g>
       </g>
     </g>
   </svg>
   </div>
   </div>
   </div>
   </div>
   </div>
   <div class="text_cell_render border-box-sizing rendered_html">
   <p>I used these software versions for the following computations:</p>
   <ul>
   <li>IPython: 0.13.1.rc2</li>
   <li>matplotlib: 1.1.1</li>
   <li>NumPy: 1.6.2</li>
   <li>SciPy: 0.10.1</li>
   <li>SymPy: 0.7.2</li>
   <li>python-control: 0.6d </li>
   </ul>
   <h1 class="ipynb">Equations of Motion</h1>
   <p>We'll start by generating the equations of motion for the system with SymPy <strong><a href="http://docs.sympy.org/dev/modules/physics/mechanics/index.html">mechanics</a></strong>. The functionality that mechanics provides is much more in depth than Mathematica's functionality. In the Mathematica example, Lagrangian mechanics were implemented manually with Mathematica's symbolic functionality. <strong>mechanics</strong> provides an assortment of functions and classes to derive the equations of motion for arbitrarily complex (i.e. configuration constraints, nonholonomic motion constraints, etc) multibody systems in a very natural way. First we import the necessary functionality from SymPy.</p>
   </div>
   <div class="cell border-box-sizing code_cell vbox">
   <div class="input hbox">
   <div class="prompt input_prompt">In&nbsp;[2]:</div>
   <div class="input_area box-flex1">
   <div class="highlight-ipynb"><pre class="ipynb"><span class="kn">from</span> <span class="nn">sympy</span> <span class="kn">import</span> <span class="n">symbols</span>
   <span class="kn">from</span> <span class="nn">sympy.physics.mechanics</span> <span class="kn">import</span> <span class="o">*</span>
   </pre></div>

   </div>
   </div>
   </div>
   <div class="text_cell_render border-box-sizing rendered_html">
   <p>Now specify the number of links, $n$. I'll start with 5 since the Wolfram folks only showed four.</p>
   </div>
   <div class="cell border-box-sizing code_cell vbox">
   <div class="input hbox">
   <div class="prompt input_prompt">In&nbsp;[3]:</div>
   <div class="input_area box-flex1">
   <div class="highlight-ipynb"><pre class="ipynb"><span class="n">n</span> <span class="o">=</span> <span class="mi">5</span>
   </pre></div>

   </div>
   </div>
   </div>
   <div class="text_cell_render border-box-sizing rendered_html">
   <p><strong>mechanics</strong> will need the generalized coordinates, generalized speeds, and the input force which are all time dependent variables and the bob masses, link lengths, and acceleration due to gravity which are all constants. Time, $t$, is also made available because we will need to differentiate with respect to time.</p>
   </div>
   <div class="cell border-box-sizing code_cell vbox">
   <div class="input hbox">
   <div class="prompt input_prompt">In&nbsp;[4]:</div>
   <div class="input_area box-flex1">
   <div class="highlight-ipynb"><pre class="ipynb"><span class="n">q</span> <span class="o">=</span> <span class="n">dynamicsymbols</span><span class="p">(</span><span class="s">&#39;q:&#39;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">n</span> <span class="o">+</span> <span class="mi">1</span><span class="p">))</span>  <span class="c"># Generalized coordinates</span>
   <span class="n">u</span> <span class="o">=</span> <span class="n">dynamicsymbols</span><span class="p">(</span><span class="s">&#39;u:&#39;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">n</span> <span class="o">+</span> <span class="mi">1</span><span class="p">))</span>  <span class="c"># Generalized speeds</span>
   <span class="n">f</span> <span class="o">=</span> <span class="n">dynamicsymbols</span><span class="p">(</span><span class="s">&#39;f&#39;</span><span class="p">)</span>                <span class="c"># Force applied to the cart</span>

   <span class="n">m</span> <span class="o">=</span> <span class="n">symbols</span><span class="p">(</span><span class="s">&#39;m:&#39;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">n</span> <span class="o">+</span> <span class="mi">1</span><span class="p">))</span>         <span class="c"># Mass of each bob</span>
   <span class="n">l</span> <span class="o">=</span> <span class="n">symbols</span><span class="p">(</span><span class="s">&#39;l:&#39;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">n</span><span class="p">))</span>             <span class="c"># Length of each link</span>
   <span class="n">g</span><span class="p">,</span> <span class="n">t</span> <span class="o">=</span> <span class="n">symbols</span><span class="p">(</span><span class="s">&#39;g t&#39;</span><span class="p">)</span>                  <span class="c"># Gravity and time</span>
   </pre></div>

   </div>
   </div>
   </div>
   <div class="text_cell_render border-box-sizing rendered_html">
   <p>Now we can create and inertial reference frame $I$ and define the point, $O$, as the origin.</p>
   </div>
   <div class="cell border-box-sizing code_cell vbox">
   <div class="input hbox">
   <div class="prompt input_prompt">In&nbsp;[5]:</div>
   <div class="input_area box-flex1">
   <div class="highlight-ipynb"><pre class="ipynb"><span class="n">I</span> <span class="o">=</span> <span class="n">ReferenceFrame</span><span class="p">(</span><span class="s">&#39;I&#39;</span><span class="p">)</span>                <span class="c"># Inertial reference frame</span>
   <span class="n">O</span> <span class="o">=</span> <span class="n">Point</span><span class="p">(</span><span class="s">&#39;O&#39;</span><span class="p">)</span>                         <span class="c"># Origin point</span>
   <span class="n">O</span><span class="o">.</span><span class="n">set_vel</span><span class="p">(</span><span class="n">I</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>                        <span class="c"># Origin&#39;s velocity is zero</span>
   </pre></div>

   </div>
   </div>
   </div>
   <div class="text_cell_render border-box-sizing rendered_html">
   <p>Secondly, we define the define the first point of the pendulum as a particle which has mass. This point can only move laterally and represents the motion of the "cart".</p>
   </div>
   <div class="cell border-box-sizing code_cell vbox">
   <div class="input hbox">
   <div class="prompt input_prompt">In&nbsp;[6]:</div>
   <div class="input_area box-flex1">
   <div class="highlight-ipynb"><pre class="ipynb"><span class="n">P0</span> <span class="o">=</span> <span class="n">Point</span><span class="p">(</span><span class="s">&#39;P0&#39;</span><span class="p">)</span>                       <span class="c"># Hinge point of top link</span>
   <span class="n">P0</span><span class="o">.</span><span class="n">set_pos</span><span class="p">(</span><span class="n">O</span><span class="p">,</span> <span class="n">q</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">*</span> <span class="n">I</span><span class="o">.</span><span class="n">x</span><span class="p">)</span>              <span class="c"># Set the position of P0    </span>
   <span class="n">P0</span><span class="o">.</span><span class="n">set_vel</span><span class="p">(</span><span class="n">I</span><span class="p">,</span> <span class="n">u</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">*</span> <span class="n">I</span><span class="o">.</span><span class="n">x</span><span class="p">)</span>              <span class="c"># Set the velocity of P0</span>
   <span class="n">Pa0</span> <span class="o">=</span> <span class="n">Particle</span><span class="p">(</span><span class="s">&#39;Pa0&#39;</span><span class="p">,</span> <span class="n">P0</span><span class="p">,</span> <span class="n">m</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>        <span class="c"># Define a particle at P0</span>
   </pre></div>

   </div>
   </div>
   </div>
   <div class="text_cell_render border-box-sizing rendered_html">
   <p>Now we can define the $n$ reference frames, particles, gravitational forces, and kinematical differential equations for each of the pendulum links. This is easily done with a loop.</p>
   </div>
   <div class="cell border-box-sizing code_cell vbox">
   <div class="input hbox">
   <div class="prompt input_prompt">In&nbsp;[7]:</div>
   <div class="input_area box-flex1">
   <div class="highlight-ipynb"><pre class="ipynb"><span class="n">frames</span> <span class="o">=</span> <span class="p">[</span><span class="n">I</span><span class="p">]</span>                              <span class="c"># List to hold the n + 1 frames</span>
   <span class="n">points</span> <span class="o">=</span> <span class="p">[</span><span class="n">P0</span><span class="p">]</span>                             <span class="c"># List to hold the n + 1 points</span>
   <span class="n">particles</span> <span class="o">=</span> <span class="p">[</span><span class="n">Pa0</span><span class="p">]</span>                         <span class="c"># List to hold the n + 1 particles</span>
   <span class="n">forces</span> <span class="o">=</span> <span class="p">[(</span><span class="n">P0</span><span class="p">,</span> <span class="n">f</span> <span class="o">*</span> <span class="n">I</span><span class="o">.</span><span class="n">x</span> <span class="o">-</span> <span class="n">m</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">*</span> <span class="n">g</span> <span class="o">*</span> <span class="n">I</span><span class="o">.</span><span class="n">y</span><span class="p">)]</span> <span class="c"># List to hold the n + 1 applied forces, including the input force, f</span>
   <span class="n">kindiffs</span> <span class="o">=</span> <span class="p">[</span><span class="n">q</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">diff</span><span class="p">(</span><span class="n">t</span><span class="p">)</span> <span class="o">-</span> <span class="n">u</span><span class="p">[</span><span class="mi">0</span><span class="p">]]</span>          <span class="c"># List to hold kinematic ODE&#39;s</span>

   <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">n</span><span class="p">):</span>
       <span class="n">Bi</span> <span class="o">=</span> <span class="n">I</span><span class="o">.</span><span class="n">orientnew</span><span class="p">(</span><span class="s">&#39;B&#39;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">i</span><span class="p">),</span> <span class="s">&#39;Axis&#39;</span><span class="p">,</span> <span class="p">[</span><span class="n">q</span><span class="p">[</span><span class="n">i</span> <span class="o">+</span> <span class="mi">1</span><span class="p">],</span> <span class="n">I</span><span class="o">.</span><span class="n">z</span><span class="p">])</span>   <span class="c"># Create a new frame</span>
       <span class="n">Bi</span><span class="o">.</span><span class="n">set_ang_vel</span><span class="p">(</span><span class="n">I</span><span class="p">,</span> <span class="n">u</span><span class="p">[</span><span class="n">i</span> <span class="o">+</span> <span class="mi">1</span><span class="p">]</span> <span class="o">*</span> <span class="n">I</span><span class="o">.</span><span class="n">z</span><span class="p">)</span>                         <span class="c"># Set angular velocity</span>
       <span class="n">frames</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Bi</span><span class="p">)</span>                                         <span class="c"># Add it to the frames list</span>

       <span class="n">Pi</span> <span class="o">=</span> <span class="n">points</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">locatenew</span><span class="p">(</span><span class="s">&#39;P&#39;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">i</span> <span class="o">+</span> <span class="mi">1</span><span class="p">),</span> <span class="n">l</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">*</span> <span class="n">Bi</span><span class="o">.</span><span class="n">x</span><span class="p">)</span>  <span class="c"># Create a new point</span>
       <span class="n">Pi</span><span class="o">.</span><span class="n">v2pt_theory</span><span class="p">(</span><span class="n">points</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">],</span> <span class="n">I</span><span class="p">,</span> <span class="n">Bi</span><span class="p">)</span>                         <span class="c"># Set the velocity</span>
       <span class="n">points</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Pi</span><span class="p">)</span>                                         <span class="c"># Add it to the points list</span>

       <span class="n">Pai</span> <span class="o">=</span> <span class="n">Particle</span><span class="p">(</span><span class="s">&#39;Pa&#39;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">i</span> <span class="o">+</span> <span class="mi">1</span><span class="p">),</span> <span class="n">Pi</span><span class="p">,</span> <span class="n">m</span><span class="p">[</span><span class="n">i</span> <span class="o">+</span> <span class="mi">1</span><span class="p">])</span>           <span class="c"># Create a new particle</span>
       <span class="n">particles</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Pai</span><span class="p">)</span>                                     <span class="c"># Add it to the particles list</span>

       <span class="n">forces</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">Pi</span><span class="p">,</span> <span class="o">-</span><span class="n">m</span><span class="p">[</span><span class="n">i</span> <span class="o">+</span> <span class="mi">1</span><span class="p">]</span> <span class="o">*</span> <span class="n">g</span> <span class="o">*</span> <span class="n">I</span><span class="o">.</span><span class="n">y</span><span class="p">))</span>                  <span class="c"># Set the force applied at the point</span>

       <span class="n">kindiffs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">q</span><span class="p">[</span><span class="n">i</span> <span class="o">+</span> <span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">diff</span><span class="p">(</span><span class="n">t</span><span class="p">)</span> <span class="o">-</span> <span class="n">u</span><span class="p">[</span><span class="n">i</span> <span class="o">+</span> <span class="mi">1</span><span class="p">])</span>              <span class="c"># Define the kinematic ODE:  dq_i / dt - u_i = 0</span>
   </pre></div>

   </div>
   </div>
   </div>
   <div class="text_cell_render border-box-sizing rendered_html">
   <p>With all of the necessary point velocities and particle masses defined, the <code>KanesMethod</code> class can be used to derive the equations of motion of the system automatically.</p>
   </div>
   <div class="cell border-box-sizing code_cell vbox">
   <div class="input hbox">
   <div class="prompt input_prompt">In&nbsp;[8]:</div>
   <div class="input_area box-flex1">
   <div class="highlight-ipynb"><pre class="ipynb"><span class="n">kane</span> <span class="o">=</span> <span class="n">KanesMethod</span><span class="p">(</span><span class="n">I</span><span class="p">,</span> <span class="n">q_ind</span><span class="o">=</span><span class="n">q</span><span class="p">,</span> <span class="n">u_ind</span><span class="o">=</span><span class="n">u</span><span class="p">,</span> <span class="n">kd_eqs</span><span class="o">=</span><span class="n">kindiffs</span><span class="p">)</span> <span class="c"># Initialize the object</span>
   <span class="n">fr</span><span class="p">,</span> <span class="n">frstar</span> <span class="o">=</span> <span class="n">kane</span><span class="o">.</span><span class="n">kanes_equations</span><span class="p">(</span><span class="n">forces</span><span class="p">,</span> <span class="n">particles</span><span class="p">)</span>     <span class="c"># Generate EoM&#39;s fr + frstar = 0</span>
   </pre></div>

   </div>
   </div>
   </div>
   <div class="text_cell_render border-box-sizing rendered_html">
   <p>The equations of motion are quite long as can been seen below. This is the general nature of most non-simple mutlibody problems. That is why a SymPy is so useful; no more mistakes in algegra, differentiation, or copying in hand written equations. </p>
   </div>
   <div class="cell border-box-sizing code_cell vbox">
   <div class="input hbox">
   <div class="prompt input_prompt">In&nbsp;[9]:</div>
   <div class="input_area box-flex1">
   <div class="highlight-ipynb"><pre class="ipynb"><span class="n">fr</span>
   </pre></div>

   </div>
   </div>
   <div class="vbox output_wrapper">
   <div class="output vbox">
   <div class="hbox output_area">
   <div class="prompt output_prompt">Out[9]:</div>
   <div class="output_subarea output_pyout">
   <pre class="ipynb">[                                                                                                 -f(t)]
   [g*l0*m1*cos(q1(t)) + g*l0*m2*cos(q1(t)) + g*l0*m3*cos(q1(t)) + g*l0*m4*cos(q1(t)) + g*l0*m5*cos(q1(t))]
   [                     g*l1*m2*cos(q2(t)) + g*l1*m3*cos(q2(t)) + g*l1*m4*cos(q2(t)) + g*l1*m5*cos(q2(t))]
   [                                          g*l2*m3*cos(q3(t)) + g*l2*m4*cos(q3(t)) + g*l2*m5*cos(q3(t))]
   [                                                               g*l3*m4*cos(q4(t)) + g*l3*m5*cos(q4(t))]
   [                                                                                    g*l4*m5*cos(q5(t))]</pre>
   </div>
   </div>
   </div>
   </div>
   </div>
   <div class="cell border-box-sizing code_cell vbox">
   <div class="input hbox">
   <div class="prompt input_prompt">In&nbsp;[10]:</div>
   <div class="input_area box-flex1">
   <div class="highlight-ipynb"><pre class="ipynb"><span class="n">frstar</span>
   </pre></div>

   </div>
   </div>
   <div class="vbox output_wrapper">
   <div class="output vbox">
   <div class="hbox output_area">
   <div class="prompt output_prompt">Out[10]:</div>
   <div class="output_subarea output_pyout">
   <pre class="ipynb">[                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    -l0*m1*u1(t)**2*cos(q1(t)) - l0*m2*u1(t)**2*cos(q1(t)) - l0*m3*u1(t)**2*cos(q1(t)) - l0*m4*u1(t)**2*cos(q1(t)) - l0*m5*u1(t)**2*cos(q1(t)) - l1*m2*u2(t)**2*cos(q2(t)) - l1*m3*u2(t)**2*cos(q2(t)) - l1*m4*u2(t)**2*cos(q2(t)) - l1*m5*u2(t)**2*cos(q2(t)) - l2*m3*u3(t)**2*cos(q3(t)) - l2*m4*u3(t)**2*cos(q3(t)) - l2*m5*u3(t)**2*cos(q3(t)) - l3*m4*u4(t)**2*cos(q4(t)) - l3*m5*u4(t)**2*cos(q4(t)) - l4*m5*u5(t)**2*cos(q5(t)) - l4*m5*sin(q5(t))*Derivative(u5(t), t) + (-l3*m4*sin(q4(t)) - l3*m5*sin(q4(t)))*Derivative(u4(t), t) + (-l2*m3*sin(q3(t)) - l2*m4*sin(q3(t)) - l2*m5*sin(q3(t)))*Derivative(u3(t), t) + (-l1*m2*sin(q2(t)) - l1*m3*sin(q2(t)) - l1*m4*sin(q2(t)) - l1*m5*sin(q2(t)))*Derivative(u2(t), t) + (-l0*m1*sin(q1(t)) - l0*m2*sin(q1(t)) - l0*m3*sin(q1(t)) - l0*m4*sin(q1(t)) - l0*m5*sin(q1(t)))*Derivative(u1(t), t) + (m0 + m1 + m2 + m3 + m4 + m5)*Derivative(u0(t), t)]
   [-l0*l1*m2*(-sin(q1(t))*cos(q2(t)) + sin(q2(t))*cos(q1(t)))*u2(t)**2 - l0*l1*m3*(-sin(q1(t))*cos(q2(t)) + sin(q2(t))*cos(q1(t)))*u2(t)**2 - l0*l1*m4*(-sin(q1(t))*cos(q2(t)) + sin(q2(t))*cos(q1(t)))*u2(t)**2 - l0*l1*m5*(-sin(q1(t))*cos(q2(t)) + sin(q2(t))*cos(q1(t)))*u2(t)**2 - l0*l2*m3*(-sin(q1(t))*cos(q3(t)) + sin(q3(t))*cos(q1(t)))*u3(t)**2 - l0*l2*m4*(-sin(q1(t))*cos(q3(t)) + sin(q3(t))*cos(q1(t)))*u3(t)**2 - l0*l2*m5*(-sin(q1(t))*cos(q3(t)) + sin(q3(t))*cos(q1(t)))*u3(t)**2 - l0*l3*m4*(-sin(q1(t))*cos(q4(t)) + sin(q4(t))*cos(q1(t)))*u4(t)**2 - l0*l3*m5*(-sin(q1(t))*cos(q4(t)) + sin(q4(t))*cos(q1(t)))*u4(t)**2 + l0*l4*m5*(sin(q1(t))*sin(q5(t)) + cos(q1(t))*cos(q5(t)))*Derivative(u5(t), t) - l0*l4*m5*(-sin(q1(t))*cos(q5(t)) + sin(q5(t))*cos(q1(t)))*u5(t)**2 + (l0*l3*m4*(sin(q1(t))*sin(q4(t)) + cos(q1(t))*cos(q4(t))) + l0*l3*m5*(sin(q1(t))*sin(q4(t)) + cos(q1(t))*cos(q4(t))))*Derivative(u4(t), t) + (l0*l2*m3*(sin(q1(t))*sin(q3(t)) + cos(q1(t))*cos(q3(t))) + l0*l2*m4*(sin(q1(t))*sin(q3(t)) + cos(q1(t))*cos(q3(t))) + l0*l2*m5*(sin(q1(t))*sin(q3(t)) + cos(q1(t))*cos(q3(t))))*Derivative(u3(t), t) + (l0*l1*m2*(sin(q1(t))*sin(q2(t)) + cos(q1(t))*cos(q2(t))) + l0*l1*m3*(sin(q1(t))*sin(q2(t)) + cos(q1(t))*cos(q2(t))) + l0*l1*m4*(sin(q1(t))*sin(q2(t)) + cos(q1(t))*cos(q2(t))) + l0*l1*m5*(sin(q1(t))*sin(q2(t)) + cos(q1(t))*cos(q2(t))))*Derivative(u2(t), t) + (l0**2*m1 + l0**2*m2 + l0**2*m3 + l0**2*m4 + l0**2*m5)*Derivative(u1(t), t) + (-l0*m1*sin(q1(t)) - l0*m2*sin(q1(t)) - l0*m3*sin(q1(t)) - l0*m4*sin(q1(t)) - l0*m5*sin(q1(t)))*Derivative(u0(t), t)]
   [                                  -l0*l1*m2*(sin(q1(t))*cos(q2(t)) - sin(q2(t))*cos(q1(t)))*u1(t)**2 - l0*l1*m3*(sin(q1(t))*cos(q2(t)) - sin(q2(t))*cos(q1(t)))*u1(t)**2 - l0*l1*m4*(sin(q1(t))*cos(q2(t)) - sin(q2(t))*cos(q1(t)))*u1(t)**2 - l0*l1*m5*(sin(q1(t))*cos(q2(t)) - sin(q2(t))*cos(q1(t)))*u1(t)**2 - l1*l2*m3*(-sin(q2(t))*cos(q3(t)) + sin(q3(t))*cos(q2(t)))*u3(t)**2 - l1*l2*m4*(-sin(q2(t))*cos(q3(t)) + sin(q3(t))*cos(q2(t)))*u3(t)**2 - l1*l2*m5*(-sin(q2(t))*cos(q3(t)) + sin(q3(t))*cos(q2(t)))*u3(t)**2 - l1*l3*m4*(-sin(q2(t))*cos(q4(t)) + sin(q4(t))*cos(q2(t)))*u4(t)**2 - l1*l3*m5*(-sin(q2(t))*cos(q4(t)) + sin(q4(t))*cos(q2(t)))*u4(t)**2 + l1*l4*m5*(sin(q2(t))*sin(q5(t)) + cos(q2(t))*cos(q5(t)))*Derivative(u5(t), t) - l1*l4*m5*(-sin(q2(t))*cos(q5(t)) + sin(q5(t))*cos(q2(t)))*u5(t)**2 + (l1*l3*m4*(sin(q2(t))*sin(q4(t)) + cos(q2(t))*cos(q4(t))) + l1*l3*m5*(sin(q2(t))*sin(q4(t)) + cos(q2(t))*cos(q4(t))))*Derivative(u4(t), t) + (l1*l2*m3*(sin(q2(t))*sin(q3(t)) + cos(q2(t))*cos(q3(t))) + l1*l2*m4*(sin(q2(t))*sin(q3(t)) + cos(q2(t))*cos(q3(t))) + l1*l2*m5*(sin(q2(t))*sin(q3(t)) + cos(q2(t))*cos(q3(t))))*Derivative(u3(t), t) + (l1**2*m2 + l1**2*m3 + l1**2*m4 + l1**2*m5)*Derivative(u2(t), t) + (-l1*m2*sin(q2(t)) - l1*m3*sin(q2(t)) - l1*m4*sin(q2(t)) - l1*m5*sin(q2(t)))*Derivative(u0(t), t) + (l0*l1*m2*(sin(q1(t))*sin(q2(t)) + cos(q1(t))*cos(q2(t))) + l0*l1*m3*(sin(q1(t))*sin(q2(t)) + cos(q1(t))*cos(q2(t))) + l0*l1*m4*(sin(q1(t))*sin(q2(t)) + cos(q1(t))*cos(q2(t))) + l0*l1*m5*(sin(q1(t))*sin(q2(t)) + cos(q1(t))*cos(q2(t))))*Derivative(u1(t), t)]
   [                                                                                                                                                                                                  -l0*l2*m3*(sin(q1(t))*cos(q3(t)) - sin(q3(t))*cos(q1(t)))*u1(t)**2 - l0*l2*m4*(sin(q1(t))*cos(q3(t)) - sin(q3(t))*cos(q1(t)))*u1(t)**2 - l0*l2*m5*(sin(q1(t))*cos(q3(t)) - sin(q3(t))*cos(q1(t)))*u1(t)**2 - l1*l2*m3*(sin(q2(t))*cos(q3(t)) - sin(q3(t))*cos(q2(t)))*u2(t)**2 - l1*l2*m4*(sin(q2(t))*cos(q3(t)) - sin(q3(t))*cos(q2(t)))*u2(t)**2 - l1*l2*m5*(sin(q2(t))*cos(q3(t)) - sin(q3(t))*cos(q2(t)))*u2(t)**2 - l2*l3*m4*(-sin(q3(t))*cos(q4(t)) + sin(q4(t))*cos(q3(t)))*u4(t)**2 - l2*l3*m5*(-sin(q3(t))*cos(q4(t)) + sin(q4(t))*cos(q3(t)))*u4(t)**2 + l2*l4*m5*(sin(q3(t))*sin(q5(t)) + cos(q3(t))*cos(q5(t)))*Derivative(u5(t), t) - l2*l4*m5*(-sin(q3(t))*cos(q5(t)) + sin(q5(t))*cos(q3(t)))*u5(t)**2 + (l2*l3*m4*(sin(q3(t))*sin(q4(t)) + cos(q3(t))*cos(q4(t))) + l2*l3*m5*(sin(q3(t))*sin(q4(t)) + cos(q3(t))*cos(q4(t))))*Derivative(u4(t), t) + (l2**2*m3 + l2**2*m4 + l2**2*m5)*Derivative(u3(t), t) + (-l2*m3*sin(q3(t)) - l2*m4*sin(q3(t)) - l2*m5*sin(q3(t)))*Derivative(u0(t), t) + (l0*l2*m3*(sin(q1(t))*sin(q3(t)) + cos(q1(t))*cos(q3(t))) + l0*l2*m4*(sin(q1(t))*sin(q3(t)) + cos(q1(t))*cos(q3(t))) + l0*l2*m5*(sin(q1(t))*sin(q3(t)) + cos(q1(t))*cos(q3(t))))*Derivative(u1(t), t) + (l1*l2*m3*(sin(q2(t))*sin(q3(t)) + cos(q2(t))*cos(q3(t))) + l1*l2*m4*(sin(q2(t))*sin(q3(t)) + cos(q2(t))*cos(q3(t))) + l1*l2*m5*(sin(q2(t))*sin(q3(t)) + cos(q2(t))*cos(q3(t))))*Derivative(u2(t), t)]
   [                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                -l0*l3*m4*(sin(q1(t))*cos(q4(t)) - sin(q4(t))*cos(q1(t)))*u1(t)**2 - l0*l3*m5*(sin(q1(t))*cos(q4(t)) - sin(q4(t))*cos(q1(t)))*u1(t)**2 - l1*l3*m4*(sin(q2(t))*cos(q4(t)) - sin(q4(t))*cos(q2(t)))*u2(t)**2 - l1*l3*m5*(sin(q2(t))*cos(q4(t)) - sin(q4(t))*cos(q2(t)))*u2(t)**2 - l2*l3*m4*(sin(q3(t))*cos(q4(t)) - sin(q4(t))*cos(q3(t)))*u3(t)**2 - l2*l3*m5*(sin(q3(t))*cos(q4(t)) - sin(q4(t))*cos(q3(t)))*u3(t)**2 + l3*l4*m5*(sin(q4(t))*sin(q5(t)) + cos(q4(t))*cos(q5(t)))*Derivative(u5(t), t) - l3*l4*m5*(-sin(q4(t))*cos(q5(t)) + sin(q5(t))*cos(q4(t)))*u5(t)**2 + (l3**2*m4 + l3**2*m5)*Derivative(u4(t), t) + (-l3*m4*sin(q4(t)) - l3*m5*sin(q4(t)))*Derivative(u0(t), t) + (l0*l3*m4*(sin(q1(t))*sin(q4(t)) + cos(q1(t))*cos(q4(t))) + l0*l3*m5*(sin(q1(t))*sin(q4(t)) + cos(q1(t))*cos(q4(t))))*Derivative(u1(t), t) + (l1*l3*m4*(sin(q2(t))*sin(q4(t)) + cos(q2(t))*cos(q4(t))) + l1*l3*m5*(sin(q2(t))*sin(q4(t)) + cos(q2(t))*cos(q4(t))))*Derivative(u2(t), t) + (l2*l3*m4*(sin(q3(t))*sin(q4(t)) + cos(q3(t))*cos(q4(t))) + l2*l3*m5*(sin(q3(t))*sin(q4(t)) + cos(q3(t))*cos(q4(t))))*Derivative(u3(t), t)]
   [                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        l0*l4*m5*(sin(q1(t))*sin(q5(t)) + cos(q1(t))*cos(q5(t)))*Derivative(u1(t), t) - l0*l4*m5*(sin(q1(t))*cos(q5(t)) - sin(q5(t))*cos(q1(t)))*u1(t)**2 + l1*l4*m5*(sin(q2(t))*sin(q5(t)) + cos(q2(t))*cos(q5(t)))*Derivative(u2(t), t) - l1*l4*m5*(sin(q2(t))*cos(q5(t)) - sin(q5(t))*cos(q2(t)))*u2(t)**2 + l2*l4*m5*(sin(q3(t))*sin(q5(t)) + cos(q3(t))*cos(q5(t)))*Derivative(u3(t), t) - l2*l4*m5*(sin(q3(t))*cos(q5(t)) - sin(q5(t))*cos(q3(t)))*u3(t)**2 + l3*l4*m5*(sin(q4(t))*sin(q5(t)) + cos(q4(t))*cos(q5(t)))*Derivative(u4(t), t) - l3*l4*m5*(sin(q4(t))*cos(q5(t)) - sin(q5(t))*cos(q4(t)))*u4(t)**2 + l4**2*m5*Derivative(u5(t), t) - l4*m5*sin(q5(t))*Derivative(u0(t), t)]</pre>
   </div>
   </div>
   </div>
   </div>
   </div>
   <div class="text_cell_render border-box-sizing rendered_html">
   <h1 class="ipynb">Simulation</h1>
   <p>Now that the symbolic equations of motion are available we can simulate the pendulum's motion. We will need some more SymPy functionality and several NumPy functions, and most importantly the integration function from SciPy, <code>odeint</code>.</p>
   </div>
   <div class="cell border-box-sizing code_cell vbox">
   <div class="input hbox">
   <div class="prompt input_prompt">In&nbsp;[11]:</div>
   <div class="input_area box-flex1">
   <div class="highlight-ipynb"><pre class="ipynb"><span class="kn">from</span> <span class="nn">sympy</span> <span class="kn">import</span> <span class="n">Dummy</span><span class="p">,</span> <span class="n">lambdify</span>
   <span class="kn">from</span> <span class="nn">numpy</span> <span class="kn">import</span> <span class="n">array</span><span class="p">,</span> <span class="n">hstack</span><span class="p">,</span> <span class="n">zeros</span><span class="p">,</span> <span class="n">linspace</span><span class="p">,</span> <span class="n">pi</span>
   <span class="kn">from</span> <span class="nn">numpy.linalg</span> <span class="kn">import</span> <span class="n">solve</span>
   <span class="kn">from</span> <span class="nn">scipy.integrate</span> <span class="kn">import</span> <span class="n">odeint</span>
   </pre></div>

   </div>
   </div>
   </div>
   <div class="text_cell_render border-box-sizing rendered_html">
   <p>First, define some numeric values for all of the constant parameters in the problem.</p>
   </div>
   <div class="cell border-box-sizing code_cell vbox">
   <div class="input hbox">
   <div class="prompt input_prompt">In&nbsp;[12]:</div>
   <div class="input_area box-flex1">
   <div class="highlight-ipynb"><pre class="ipynb"><span class="n">arm_length</span> <span class="o">=</span> <span class="mf">1.</span> <span class="o">/</span> <span class="n">n</span>                          <span class="c"># The maximum length of the pendulum is 1 meter</span>
   <span class="n">bob_mass</span> <span class="o">=</span> <span class="mf">0.01</span> <span class="o">/</span> <span class="n">n</span>                          <span class="c"># The maximum mass of the bobs is 10 grams</span>
   <span class="n">parameters</span> <span class="o">=</span> <span class="p">[</span><span class="n">g</span><span class="p">,</span> <span class="n">m</span><span class="p">[</span><span class="mi">0</span><span class="p">]]</span>                       <span class="c"># Parameter definitions starting with gravity and the first bob</span>
   <span class="n">parameter_vals</span> <span class="o">=</span> <span class="p">[</span><span class="mf">9.81</span><span class="p">,</span> <span class="mf">0.01</span> <span class="o">/</span> <span class="n">n</span><span class="p">]</span>            <span class="c"># Numerical values for the first two</span>
   <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">n</span><span class="p">):</span>                           <span class="c"># Then each mass and length</span>
       <span class="n">parameters</span> <span class="o">+=</span> <span class="p">[</span><span class="n">l</span><span class="p">[</span><span class="n">i</span><span class="p">],</span> <span class="n">m</span><span class="p">[</span><span class="n">i</span> <span class="o">+</span> <span class="mi">1</span><span class="p">]]</span>            
       <span class="n">parameter_vals</span> <span class="o">+=</span> <span class="p">[</span><span class="n">arm_length</span><span class="p">,</span> <span class="n">bob_mass</span><span class="p">]</span>
   </pre></div>

   </div>
   </div>
   </div>
   <div class="text_cell_render border-box-sizing rendered_html">
   <p>Mathematica has a really nice <code>NDSolve</code> function for quickly integrating their symbolic differential equations. We have plans to develop something similar for SymPy but haven't found the development time yet to do it properly. So the next bit isn't as clean as we'd like but you can make use of SymPy's lambdify function to create functions that will evaluate the mass matrix, $M$, and forcing vector, $\bar{f}$ from $M\dot{u} = \bar{f}(q, \dot{q}, u, t)$ as a NumPy function. We make use of dummy symbols to replace the time varying functions in the SymPy equations a simple dummy symbol. </p>
   </div>
   <div class="cell border-box-sizing code_cell vbox">
   <div class="input hbox">
   <div class="prompt input_prompt">In&nbsp;[13]:</div>
   <div class="input_area box-flex1">
   <div class="highlight-ipynb"><pre class="ipynb"><span class="n">dynamic</span> <span class="o">=</span> <span class="n">q</span> <span class="o">+</span> <span class="n">u</span>                                                <span class="c"># Make a list of the states</span>
   <span class="n">dynamic</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">f</span><span class="p">)</span>                                              <span class="c"># Add the input force</span>
   <span class="n">dummy_symbols</span> <span class="o">=</span> <span class="p">[</span><span class="n">Dummy</span><span class="p">()</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">dynamic</span><span class="p">]</span>                     <span class="c"># Create a dummy symbol for each variable</span>
   <span class="n">dummy_dict</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">(</span><span class="nb">zip</span><span class="p">(</span><span class="n">dynamic</span><span class="p">,</span> <span class="n">dummy_symbols</span><span class="p">))</span>                 
   <span class="n">kindiff_dict</span> <span class="o">=</span> <span class="n">kane</span><span class="o">.</span><span class="n">kindiffdict</span><span class="p">()</span>                              <span class="c"># Get the solved kinematical differential equations</span>
   <span class="n">M</span> <span class="o">=</span> <span class="n">kane</span><span class="o">.</span><span class="n">mass_matrix_full</span><span class="o">.</span><span class="n">subs</span><span class="p">(</span><span class="n">kindiff_dict</span><span class="p">)</span><span class="o">.</span><span class="n">subs</span><span class="p">(</span><span class="n">dummy_dict</span><span class="p">)</span>  <span class="c"># Substitute into the mass matrix </span>
   <span class="n">F</span> <span class="o">=</span> <span class="n">kane</span><span class="o">.</span><span class="n">forcing_full</span><span class="o">.</span><span class="n">subs</span><span class="p">(</span><span class="n">kindiff_dict</span><span class="p">)</span><span class="o">.</span><span class="n">subs</span><span class="p">(</span><span class="n">dummy_dict</span><span class="p">)</span>      <span class="c"># Substitute into the forcing vector</span>
   <span class="n">M_func</span> <span class="o">=</span> <span class="n">lambdify</span><span class="p">(</span><span class="n">dummy_symbols</span> <span class="o">+</span> <span class="n">parameters</span><span class="p">,</span> <span class="n">M</span><span class="p">)</span>               <span class="c"># Create a callable function to evaluate the mass matrix </span>
   <span class="n">F_func</span> <span class="o">=</span> <span class="n">lambdify</span><span class="p">(</span><span class="n">dummy_symbols</span> <span class="o">+</span> <span class="n">parameters</span><span class="p">,</span> <span class="n">F</span><span class="p">)</span>               <span class="c"># Create a callable function to evaluate the forcing vector </span>
   </pre></div>

   </div>
   </div>
   </div>
   <div class="text_cell_render border-box-sizing rendered_html">
   <p>To integrate the ODE's we need to define a function that returns the derivatives of the states given the current state and time.</p>
   </div>
   <div class="cell border-box-sizing code_cell vbox">
   <div class="input hbox">
   <div class="prompt input_prompt">In&nbsp;[14]:</div>
   <div class="input_area box-flex1">
   <div class="highlight-ipynb"><pre class="ipynb"><span class="k">def</span> <span class="nf">right_hand_side</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">t</span><span class="p">,</span> <span class="n">args</span><span class="p">):</span>
       <span class="sd">&quot;&quot;&quot;Returns the derivatives of the states.</span>

   <span class="sd">    Parameters</span>
   <span class="sd">    ----------</span>
   <span class="sd">    x : ndarray, shape(2 * (n + 1))</span>
   <span class="sd">        The current state vector.</span>
   <span class="sd">    t : float</span>
   <span class="sd">        The current time.</span>
   <span class="sd">    args : ndarray</span>
   <span class="sd">        The constants.</span>

   <span class="sd">    Returns</span>
   <span class="sd">    -------</span>
   <span class="sd">    dx : ndarray, shape(2 * (n + 1))</span>
   <span class="sd">        The derivative of the state.</span>
   <span class="sd">    </span>
   <span class="sd">    &quot;&quot;&quot;</span>
       <span class="n">u</span> <span class="o">=</span> <span class="mf">0.0</span>                              <span class="c"># The input force is always zero     </span>
       <span class="n">arguments</span> <span class="o">=</span> <span class="n">hstack</span><span class="p">((</span><span class="n">x</span><span class="p">,</span> <span class="n">u</span><span class="p">,</span> <span class="n">args</span><span class="p">))</span>     <span class="c"># States, input, and parameters</span>
       <span class="n">dx</span> <span class="o">=</span> <span class="n">array</span><span class="p">(</span><span class="n">solve</span><span class="p">(</span><span class="n">M_func</span><span class="p">(</span><span class="o">*</span><span class="n">arguments</span><span class="p">),</span> <span class="c"># Solving for the derivatives</span>
           <span class="n">F_func</span><span class="p">(</span><span class="o">*</span><span class="n">arguments</span><span class="p">)))</span><span class="o">.</span><span class="n">T</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>

       <span class="k">return</span> <span class="n">dx</span>
   </pre></div>

   </div>
   </div>
   </div>
   <div class="text_cell_render border-box-sizing rendered_html">
   <p>Now that we have the right hand side function, the initial conditions are set such that the pendulum is in the vertical equilibrium and a slight initial rate is set for each speed to ensure the pendulum falls. The equations can then be integrated with SciPy's <code>odeint</code> function given a time series.</p>
   </div>
   <div class="cell border-box-sizing code_cell vbox">
   <div class="input hbox">
   <div class="prompt input_prompt">In&nbsp;[15]:</div>
   <div class="input_area box-flex1">
   <div class="highlight-ipynb"><pre class="ipynb"><span class="n">x0</span> <span class="o">=</span> <span class="n">hstack</span><span class="p">((</span> <span class="mi">0</span><span class="p">,</span> <span class="n">pi</span> <span class="o">/</span> <span class="mi">2</span> <span class="o">*</span> <span class="n">ones</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">q</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span><span class="p">),</span> <span class="mf">1e-3</span> <span class="o">*</span> <span class="n">ones</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">u</span><span class="p">))</span> <span class="p">))</span> <span class="c"># Initial conditions, q and u</span>
   <span class="n">t</span> <span class="o">=</span> <span class="n">linspace</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">10</span><span class="p">,</span> <span class="mi">1000</span><span class="p">)</span>                                          <span class="c"># Time vector</span>
   <span class="n">y</span> <span class="o">=</span> <span class="n">odeint</span><span class="p">(</span><span class="n">right_hand_side</span><span class="p">,</span> <span class="n">x0</span><span class="p">,</span> <span class="n">t</span><span class="p">,</span> <span class="n">args</span><span class="o">=</span><span class="p">(</span><span class="n">parameter_vals</span><span class="p">,))</span>         <span class="c"># Actual integration</span>
   </pre></div>

   </div>
   </div>
   </div>
   <div class="text_cell_render border-box-sizing rendered_html">
   <h1 class="ipynb">Plotting</h1>
   <p>The results of the simulation can be plotted with matplotlib.</p>
   </div>
   <div class="cell border-box-sizing code_cell vbox">
   <div class="input hbox">
   <div class="prompt input_prompt">In&nbsp;[16]:</div>
   <div class="input_area box-flex1">
   <div class="highlight-ipynb"><pre class="ipynb"><span class="n">lines</span> <span class="o">=</span> <span class="n">plot</span><span class="p">(</span><span class="n">t</span><span class="p">,</span> <span class="n">y</span><span class="p">[:,</span> <span class="p">:</span><span class="n">y</span><span class="o">.</span><span class="n">shape</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="o">/</span> <span class="mi">2</span><span class="p">])</span>
   <span class="n">lab</span> <span class="o">=</span> <span class="n">xlabel</span><span class="p">(</span><span class="s">&#39;Time [sec]&#39;</span><span class="p">)</span>
   <span class="n">leg</span> <span class="o">=</span> <span class="n">legend</span><span class="p">(</span><span class="n">dynamic</span><span class="p">[:</span><span class="n">y</span><span class="o">.</span><span class="n">shape</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="o">/</span> <span class="mi">2</span><span class="p">])</span>
   </pre></div>

   </div>
   </div>
   <div class="vbox output_wrapper">
   <div class="output vbox">
   <div class="hbox output_area">
   <div class="prompt output_prompt"></div>
   <div class="output_subarea output_display_data">
   <img src="data:image/png;base64,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
   AAAASUVORK5CYII=
   "></img>
   </div>
   </div>
   </div>
   </div>
   </div>
   <div class="cell border-box-sizing code_cell vbox">
   <div class="input hbox">
   <div class="prompt input_prompt">In&nbsp;[17]:</div>
   <div class="input_area box-flex1">
   <div class="highlight-ipynb"><pre class="ipynb"><span class="n">lines</span> <span class="o">=</span> <span class="n">plot</span><span class="p">(</span><span class="n">t</span><span class="p">,</span> <span class="n">y</span><span class="p">[:,</span> <span class="n">y</span><span class="o">.</span><span class="n">shape</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="o">/</span> <span class="mi">2</span><span class="p">:])</span>
   <span class="n">lab</span> <span class="o">=</span> <span class="n">xlabel</span><span class="p">(</span><span class="s">&#39;Time [sec]&#39;</span><span class="p">)</span>
   <span class="n">leg</span> <span class="o">=</span> <span class="n">legend</span><span class="p">(</span><span class="n">dynamic</span><span class="p">[</span><span class="n">y</span><span class="o">.</span><span class="n">shape</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="o">/</span> <span class="mi">2</span><span class="p">:])</span>
   </pre></div>

   </div>
   </div>
   <div class="vbox output_wrapper">
   <div class="output vbox">
   <div class="hbox output_area">
   <div class="prompt output_prompt"></div>
   <div class="output_subarea output_display_data">
   <img src="data:image/png;base64,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
   RU5ErkJggg==
   "></img>
   </div>
   </div>
   </div>
   </div>
   </div>
   <div class="text_cell_render border-box-sizing rendered_html">
   <h1 class="ipynb">Animation</h1>
   <p>matplotlib now includes very nice animation functions for animating matplotlib plots. First we import the necessary functions for creating the animation.</p>
   </div>
   <div class="cell border-box-sizing code_cell vbox">
   <div class="input hbox">
   <div class="prompt input_prompt">In&nbsp;[18]:</div>
   <div class="input_area box-flex1">
   <div class="highlight-ipynb"><pre class="ipynb"><span class="kn">from</span> <span class="nn">numpy</span> <span class="kn">import</span> <span class="n">zeros</span><span class="p">,</span> <span class="n">cos</span><span class="p">,</span> <span class="n">sin</span><span class="p">,</span> <span class="n">arange</span><span class="p">,</span> <span class="n">around</span>
   <span class="kn">from</span> <span class="nn">matplotlib</span> <span class="kn">import</span> <span class="n">pyplot</span> <span class="k">as</span> <span class="n">plt</span>
   <span class="kn">from</span> <span class="nn">matplotlib</span> <span class="kn">import</span> <span class="n">animation</span>
   <span class="kn">from</span> <span class="nn">matplotlib.patches</span> <span class="kn">import</span> <span class="n">Rectangle</span>
   </pre></div>

   </div>
   </div>
   </div>
   <div class="text_cell_render border-box-sizing rendered_html">
   <p>The following function was modeled from Jake Vanderplas's <a href="http://jakevdp.github.com/blog/2012/08/18/matplotlib-animation-tutorial/">post on matplotlib animations</a>.</p>
   </div>
   <div class="cell border-box-sizing code_cell vbox">
   <div class="input hbox">
   <div class="prompt input_prompt">In&nbsp;[19]:</div>
   <div class="input_area box-flex1">
   <div class="highlight-ipynb"><pre class="ipynb"><span class="k">def</span> <span class="nf">animate_pendulum</span><span class="p">(</span><span class="n">t</span><span class="p">,</span> <span class="n">states</span><span class="p">,</span> <span class="n">length</span><span class="p">,</span> <span class="n">filename</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span>
       <span class="sd">&quot;&quot;&quot;Animates the n-pendulum and optionally saves it to file.</span>

   <span class="sd">    Parameters</span>
   <span class="sd">    ----------</span>
   <span class="sd">    t : ndarray, shape(m)</span>
   <span class="sd">        Time array.</span>
   <span class="sd">    states: ndarray, shape(m,p)</span>
   <span class="sd">        State time history.</span>
   <span class="sd">    length: float</span>
   <span class="sd">        The length of the pendulum links.</span>
   <span class="sd">    filename: string or None, optional</span>
   <span class="sd">        If true a movie file will be saved of the animation. This may take some time.</span>

   <span class="sd">    Returns</span>
   <span class="sd">    -------</span>
   <span class="sd">    fig : matplotlib.Figure</span>
   <span class="sd">        The figure.</span>
   <span class="sd">    anim : matplotlib.FuncAnimation</span>
   <span class="sd">        The animation.</span>

   <span class="sd">    &quot;&quot;&quot;</span>
       <span class="c"># the number of pendulum bobs</span>
       <span class="n">numpoints</span> <span class="o">=</span> <span class="n">states</span><span class="o">.</span><span class="n">shape</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="o">/</span> <span class="mi">2</span>

       <span class="c"># first set up the figure, the axis, and the plot elements we want to animate</span>
       <span class="n">fig</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">()</span>

       <span class="c"># some dimesions</span>
       <span class="n">cart_width</span> <span class="o">=</span> <span class="mf">0.4</span>
       <span class="n">cart_height</span> <span class="o">=</span> <span class="mf">0.2</span>

       <span class="c"># set the limits based on the motion</span>
       <span class="n">xmin</span> <span class="o">=</span> <span class="n">around</span><span class="p">(</span><span class="n">states</span><span class="p">[:,</span> <span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">min</span><span class="p">()</span> <span class="o">-</span> <span class="n">cart_width</span> <span class="o">/</span> <span class="mf">2.0</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
       <span class="n">xmax</span> <span class="o">=</span> <span class="n">around</span><span class="p">(</span><span class="n">states</span><span class="p">[:,</span> <span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">max</span><span class="p">()</span> <span class="o">+</span> <span class="n">cart_width</span> <span class="o">/</span> <span class="mf">2.0</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>

       <span class="c"># create the axes</span>
       <span class="n">ax</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">axes</span><span class="p">(</span><span class="n">xlim</span><span class="o">=</span><span class="p">(</span><span class="n">xmin</span><span class="p">,</span> <span class="n">xmax</span><span class="p">),</span> <span class="n">ylim</span><span class="o">=</span><span class="p">(</span><span class="o">-</span><span class="mf">1.1</span><span class="p">,</span> <span class="mf">1.1</span><span class="p">),</span> <span class="n">aspect</span><span class="o">=</span><span class="s">&#39;equal&#39;</span><span class="p">)</span>

       <span class="c"># display the current time</span>
       <span class="n">time_text</span> <span class="o">=</span> <span class="n">ax</span><span class="o">.</span><span class="n">text</span><span class="p">(</span><span class="mf">0.04</span><span class="p">,</span> <span class="mf">0.9</span><span class="p">,</span> <span class="s">&#39;&#39;</span><span class="p">,</span> <span class="n">transform</span><span class="o">=</span><span class="n">ax</span><span class="o">.</span><span class="n">transAxes</span><span class="p">)</span>

       <span class="c"># create a rectangular cart</span>
       <span class="n">rect</span> <span class="o">=</span> <span class="n">Rectangle</span><span class="p">([</span><span class="n">states</span><span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">]</span> <span class="o">-</span> <span class="n">cart_width</span> <span class="o">/</span> <span class="mf">2.0</span><span class="p">,</span> <span class="o">-</span><span class="n">cart_height</span> <span class="o">/</span> <span class="mi">2</span><span class="p">],</span>
           <span class="n">cart_width</span><span class="p">,</span> <span class="n">cart_height</span><span class="p">,</span> <span class="n">fill</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s">&#39;red&#39;</span><span class="p">,</span> <span class="n">ec</span><span class="o">=</span><span class="s">&#39;black&#39;</span><span class="p">)</span>
       <span class="n">ax</span><span class="o">.</span><span class="n">add_patch</span><span class="p">(</span><span class="n">rect</span><span class="p">)</span>

       <span class="c"># blank line for the pendulum</span>
       <span class="n">line</span><span class="p">,</span> <span class="o">=</span> <span class="n">ax</span><span class="o">.</span><span class="n">plot</span><span class="p">([],</span> <span class="p">[],</span> <span class="n">lw</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span> <span class="n">marker</span><span class="o">=</span><span class="s">&#39;o&#39;</span><span class="p">,</span> <span class="n">markersize</span><span class="o">=</span><span class="mi">6</span><span class="p">)</span>

       <span class="c"># initialization function: plot the background of each frame</span>
       <span class="k">def</span> <span class="nf">init</span><span class="p">():</span>
           <span class="n">time_text</span><span class="o">.</span><span class="n">set_text</span><span class="p">(</span><span class="s">&#39;&#39;</span><span class="p">)</span>
           <span class="n">rect</span><span class="o">.</span><span class="n">set_xy</span><span class="p">((</span><span class="mf">0.0</span><span class="p">,</span> <span class="mf">0.0</span><span class="p">))</span>
           <span class="n">line</span><span class="o">.</span><span class="n">set_data</span><span class="p">([],</span> <span class="p">[])</span>
           <span class="k">return</span> <span class="n">time_text</span><span class="p">,</span> <span class="n">rect</span><span class="p">,</span> <span class="n">line</span><span class="p">,</span>

       <span class="c"># animation function: update the objects</span>
       <span class="k">def</span> <span class="nf">animate</span><span class="p">(</span><span class="n">i</span><span class="p">):</span>
           <span class="n">time_text</span><span class="o">.</span><span class="n">set_text</span><span class="p">(</span><span class="s">&#39;time = {:2.2f}&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">t</span><span class="p">[</span><span class="n">i</span><span class="p">]))</span>
           <span class="n">rect</span><span class="o">.</span><span class="n">set_xy</span><span class="p">((</span><span class="n">states</span><span class="p">[</span><span class="n">i</span><span class="p">,</span> <span class="mi">0</span><span class="p">]</span> <span class="o">-</span> <span class="n">cart_width</span> <span class="o">/</span> <span class="mf">2.0</span><span class="p">,</span> <span class="o">-</span><span class="n">cart_height</span> <span class="o">/</span> <span class="mi">2</span><span class="p">))</span>
           <span class="n">x</span> <span class="o">=</span> <span class="n">hstack</span><span class="p">((</span><span class="n">states</span><span class="p">[</span><span class="n">i</span><span class="p">,</span> <span class="mi">0</span><span class="p">],</span> <span class="n">zeros</span><span class="p">((</span><span class="n">numpoints</span> <span class="o">-</span> <span class="mi">1</span><span class="p">))))</span>
           <span class="n">y</span> <span class="o">=</span> <span class="n">zeros</span><span class="p">((</span><span class="n">numpoints</span><span class="p">))</span>
           <span class="k">for</span> <span class="n">j</span> <span class="ow">in</span> <span class="n">arange</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">numpoints</span><span class="p">):</span>
               <span class="n">x</span><span class="p">[</span><span class="n">j</span><span class="p">]</span> <span class="o">=</span> <span class="n">x</span><span class="p">[</span><span class="n">j</span> <span class="o">-</span> <span class="mi">1</span><span class="p">]</span> <span class="o">+</span> <span class="n">length</span> <span class="o">*</span> <span class="n">cos</span><span class="p">(</span><span class="n">states</span><span class="p">[</span><span class="n">i</span><span class="p">,</span> <span class="n">j</span><span class="p">])</span>
               <span class="n">y</span><span class="p">[</span><span class="n">j</span><span class="p">]</span> <span class="o">=</span> <span class="n">y</span><span class="p">[</span><span class="n">j</span> <span class="o">-</span> <span class="mi">1</span><span class="p">]</span> <span class="o">+</span> <span class="n">length</span> <span class="o">*</span> <span class="n">sin</span><span class="p">(</span><span class="n">states</span><span class="p">[</span><span class="n">i</span><span class="p">,</span> <span class="n">j</span><span class="p">])</span>
           <span class="n">line</span><span class="o">.</span><span class="n">set_data</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">)</span>
           <span class="k">return</span> <span class="n">time_text</span><span class="p">,</span> <span class="n">rect</span><span class="p">,</span> <span class="n">line</span><span class="p">,</span>

       <span class="c"># call the animator function</span>
       <span class="n">anim</span> <span class="o">=</span> <span class="n">animation</span><span class="o">.</span><span class="n">FuncAnimation</span><span class="p">(</span><span class="n">fig</span><span class="p">,</span> <span class="n">animate</span><span class="p">,</span> <span class="n">frames</span><span class="o">=</span><span class="nb">len</span><span class="p">(</span><span class="n">t</span><span class="p">),</span> <span class="n">init_func</span><span class="o">=</span><span class="n">init</span><span class="p">,</span>
               <span class="n">interval</span><span class="o">=</span><span class="n">t</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span> <span class="o">/</span> <span class="nb">len</span><span class="p">(</span><span class="n">t</span><span class="p">)</span> <span class="o">*</span> <span class="mi">1000</span><span class="p">,</span> <span class="n">blit</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span> <span class="n">repeat</span><span class="o">=</span><span class="bp">False</span><span class="p">)</span>

       <span class="c"># save the animation if a filename is given</span>
       <span class="k">if</span> <span class="n">filename</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span>
           <span class="n">anim</span><span class="o">.</span><span class="n">save</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="n">fps</span><span class="o">=</span><span class="mi">30</span><span class="p">,</span> <span class="n">codec</span><span class="o">=</span><span class="s">&#39;libx264&#39;</span><span class="p">)</span>
   </pre></div>

   </div>
   </div>
   </div>
   <div class="text_cell_render border-box-sizing rendered_html">
   <p>Now we can create the animation of the pendulum. This animation will show the open loop dynamics.</p>
   </div>
   <div class="cell border-box-sizing code_cell vbox">
   <div class="input hbox">
   <div class="prompt input_prompt">In&nbsp;[20]:</div>
   <div class="input_area box-flex1">
   <div class="highlight-ipynb"><pre class="ipynb"><span class="n">animate_pendulum</span><span class="p">(</span><span class="n">t</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">arm_length</span><span class="p">,</span> <span class="n">filename</span><span class="o">=</span><span class="s">&quot;open-loop.ogv&quot;</span><span class="p">)</span>
   <span class="n">animate_pendulum</span><span class="p">(</span><span class="n">t</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">arm_length</span><span class="p">,</span> <span class="n">filename</span><span class="o">=</span><span class="s">&quot;open-loop.mp4&quot;</span><span class="p">)</span>
   </pre></div>

   </div>
   </div>
   <div class="vbox output_wrapper">
   <div class="output vbox">
   <div class="hbox output_area">
   <div class="prompt output_prompt"></div>
   <div class="output_subarea output_display_data">
   <img src="data:image/png;base64,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
   SUVORK5CYII=
   "></img>
   </div>
   </div>
   <div class="hbox output_area">
   <div class="prompt output_prompt"></div>
   <div class="output_subarea output_display_data">
   <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAKIAAAD5CAYAAACku+4vAAAABHNCSVQICAgIfAhkiAAAAAlwSFlz
   AAALEgAACxIB0t1+/AAAFXxJREFUeJzt3X9Q0/f9B/Bn+DEdvwQqRBu4sSVxqGBgk2O7fm3xaESg
   UDut0F072lrLbFds3dnedft+hW5anPVWxdraXevpzlM7aytXflTXmdoWgVZx3Gp7RSc2QUyVQAUn
   8sPX94+UjJCEfCAJeSd5Pe5yJp+8P+/PG3ny+ZH3+5O3jIgIjHlZkLcbwBjAQWSC4CAyIXAQmRA4
   iEwIId5uAADIZDJvN4FNgfE+oBFmj0hEbnts2LBB6Pp8oY3urs8ZYYLIAhsHkQnBL4OYlZUldH2e
   qFP0+pyRidDFJ5PJJJ1HMN/l7Hfsl3tE5ntcCuKjjz4KuVyO1NRUh2XKysqgVquh0WjQ0tLiyuaY
   H3MpiI888gjq6+sdvl9bW4tz586hra0Nr7/+OtasWePK5pgfcymIixYtQkxMjMP3q6urUVJSAgDI
   zMxET08PjEajK5tkfsqjPSsdHR1ITEy0vE5ISIDBYIBcLrcpW15ebnmelZU15VdtzL10Oh10Op3k
   8h7v4ht7peSoO290EJnvG7szqaioGLe8R6+aFQoF9Hq95bXBYIBCofDkJpmP8mgQCwsLsXfvXgBA
   Y2MjoqOj7R6WGXPp0PzAAw/gww8/xNWrV5GYmIiKigoMDg4CAEpLS5GXl4fa2lqoVCqEh4dj9+7d
   bmk080MkAHvN6OnpoZ07d1ped3R00IoVK6ayWXY9//zzlJiYSBEREVbL+/v7aeXKlaRSqSgzM5Pa
   29vtrv/ZZ59RSkoKqVQqKisrm/D6vspZ1IQN4oULFyglJcULrRlfU1MTdXZ22gTxlVdeoTVr1hAR
   0YEDB6ioqMju+hkZGdTU1ERERLm5uVRXVzeh9X2VzwaxqKiIvv/971NaWho9++yz1N7ebgnm7t27
   6d577yWtVktJSUlUVVVFW7ZsofT0dPrZz35GJpOJiIjOnTtHS5cupZ/+9Ke0aNEi+vLLL93W5rFB
   zMnJocbGRiIiGhwcpJkzZ9qsc+nSJUpOTra83r9/P5WWlkpe35c5C6IQI7Tt2bx5Mz7//HNLt2B7
   e7vV+59//jnOnDmDGzduQKlUYsuWLTh9+jTWrVuHvXv3Yu3atXj88cexa9cuqFQqNDU14YknnsAH
   H3xgVY9Op8Mzzzxjs/3w8HB8/PHHkts7+jPTkJAQzJgxAyaTCbGxsVZlEhISLK8VCgU6Ojokr+/P
   hA0iORmNs3jxYoSHhyM8PBzR0dEoKCgAAKSmpqK1tRXXr19HQ0MD7r//fss6AwMDNvVkZWVxH7gA
   hA2iM9OmTbM8DwoKsrwOCgrC0NAQbt26hZiYGKchO378ONatW2ezPCwsDJ988onk9igUCnz99de4
   /fbbMTQ0hG+//dZmb6ZQKGAwGCyvDQaDZQ8pZX1/JuwwsMjISPT29k54vZE9aWRkJH74wx/i0KFD
   luWtra025RcvXoyWlhabx0RCCJg/M92zZw8A4NChQ8jOzrYpM3v2bERFRaGpqQlEhL/+9a+49957
   Ja/vz4QN4m233YY77rgDqampeO655yCTySzdg6Ofj7we/Xzk9b59+/DGG28gLS0NKSkpqK6udrld
   zz77LBITE3Hjxg0kJibihRdeAACsWrUKXV1dUKvVePnll1FZWWlZJz093fJ8586deOyxx6BWq6FS
   qbB06VKn6wcCHqHNpgSP0GY+gYPIhMBBZELgIDIhcBCZEDiITAgcRCYEDiITAgeRCYGDyITAQWRC
   4CAyIXAQmRA4iEwIHEQmBA4iEwIHkQmBg8iEwEFkQuAgMiFwEJkQOIhMCBxEJgQOIhMCB5EJgYPI
   hMBBZELgIDIhcBCZEDiITAgcRCYEDiITAgeRCYGDyITgchDr6+uRnJwMtVqNzZs327yv0+kwY8YM
   pKenIz09HX/84x9d3STzR67MJjQ0NERKpZIuXLhAAwMDpNFo6OzZs1Zljh8/TgUFBePW42IzmA9w
   9jt2aZ6V5uZmqFQqJCUlAQCKi4tx5MgRzJ07d2zYndbFM9j7lymdwX70tF0AkJCQgKamJqsyMpkM
   DQ0N0Gg0UCgUeOmllzBv3jybungGe/8y0RnsXQri6PlNHPnJT34CvV6PsLAw1NXVYdmyZfjqq69c
   2SzzQy5drCgUCuj1estrvV5vNekhYJ4BKiwsDACQm5uLwcFBmEwmVzbL/JBLQVy4cCHa2trQ3t6O
   gYEBHDx4EIWFhVZljEaj5RyxubkZRBRQc8wxaVw6NIeEhGDHjh3IycnB8PAwVq1ahblz52LXrl0A
   gNLSUhw6dAivvvoqQkJCEBYWhgMHDril4cy/8BRobErwFGjMJ3AQmRA4iEwIHEQmBA4iEwIHkQmB
   g8iEwEFkQuAgMiFwEJkQOIhMCC4NemD/VVNzAtu3H8XNmyGYNm0IZWVLkJ9/p7eb5TM4iG5QU3MC
   a9e+j/PnN1qWnT//OwDgMErEh2Y32L79qFUIAeD8+Y2oqjrmpRb5Hg6iG9y8af/AYjQGT3FLfBcH
   0Q2mTRuyu/zMmWEUFwOj7qZgDnAQ3aCsbAmUyt9ZLQsKeh7f+54WBw8CP/4x8Ic/ADdueKmBPoBH
   aLtJTc0JVFUdg9EYjDNnhqFWa/H3v9+J9euBt94yl0lKArZuBe67D5BwA6RfcfY75iC6mdEIzJoF
   REcDJpM5cB9+CJSVAa2t5jLZ2cC2bcD8+d5t61TiWwWmWHw8EBkJ9PQAXV3mZXfdBZw6BezcCcTG
   Ah98AGg0wNq1QHe3d9srCg6im8lkgFptfn7u3H+Xh4QAa9YAbW3Ak08CRMD27eayr78ODA97p72i
   4CB6gEpl/retzfa92Fhgxw6gpQXIyjLvNUtLgYwM4OOPzeeaOTm/R1ZWOXJyfo+amhNT2nZv4Z4V
   DxjZI9oL4ogFC4B//AN4+23gt781B3PRohOIiHgffX2B10PDe0QPkBJEwHwYX7EC+OILYMMGQCY7
   ahVCIHB6aDiIHjByaB59jjiesDCgvBzIzLR/gOrv9/8eGg6iB4zeI07kU6moKPs9NNOn+/+VDAfR
   A+LigKgo4NtvgatXpa9nr4dGqXweTz2ldXMLxcMXKx4gk5kPz6dPmw/PcXHS1hu5INm69X9x/Hgw
   QkOHsW3bUr+/UAG4Z8VjiouBgweBPXuAX/1qYuteuWL+YHzmTPNzf8A9K14i9crZnpF+aD/72xwX
   B9FDJnrlPNpIEG/dcl97RMfniB5QU3MCO3ceBRCC2toh1NRM7P6VoO92D4G0R+QgutnY+1euXQPW
   rp1Y70gg7hH50Oxm7rh/JRD3iHzV7CaxUVHo7u0FcBcAnZ0SWQA+lFhbBIBeAH0AIt3RPMRERsJ0
   7Zpb6poMvmqeIt29vSAAS3Dd7vs5uA4CJD36YD4mh0EmeR1nD/Mfibg4iG5Whi+hRJHVsplYjafw
   peQ6zPEDbgXQr4cvVtwsH30AalGFDHyBFHyNBORYlksT9N0ekRA4N7YEzp/cFMpHH+rxGdYhCsAf
   EIMFE1o/EPeIgfOTekEczP1z3yB+QuvxHpG5VTy+AQBcgcRRD98Z2SNyECfA2Qz2AFBWVga1Wg2N
   RoOWlhZXN+kzRoI4kT1iDSKQh3QA5RjGBtQgwkOtE4wrs5JLmcG+pqaGcnNziYiosbGRMjMzbepx
   sRlCgPnzZ6vHJcwigCgORpv37D3eQwQpsdJqsRIr6T1ESFp/vIe3/4+dbd+lPeLoGexDQ0MtM9iP
   Vl1djZKSEgBAZmYmenp6YDQaXdmsz5gJ86jYLtyGYQkHn+1IxnkctFp2HgdRhWSPtE8kHp/B3l4Z
   g8EAuVxuVW70DPZjZz/3VaEYQiy6YMJtMCEWcRh/uPZNhNtd3u9guch0Oh10Op3k8h6fwR6ATdeO
   vfVGB9GfxOEKTLgN3yDeaRCnOeiVme5gucjG7kwqKirGLe/xGezHljEYDFAoFK5s1qdM5MrZXq+M
   Eisn1Cvjqzw+g31hYSH27t0LAGhsbER0dLTNYdmfTeTKOR992IZa5CADdyELOcjANtRNqFfGV3l8
   Bvu8vDzU1tZCpVIhPDwcu3fvdkvDfcVEP9TORx/y8ZknmyQkHgbmJjLZyMfQ1jagHC9gA/4PFahA
   +VQ3y0IG23P1Kd0+DwPzrsl28wUaDqIH1SACf8FFAOU4jFOB00syCTwMzENqEIG1yLN8QP0NgLXo
   BVAbEBcfE8XniG4y9hwxBwtxFJ/alMtBBuq9cDEi+jki7xHdJCYyEjKr4fj2e0PeR7hXxtTERLrn
   3hdP4XNENzFduwYisjyWLPkfu+VychZZlZuqhzdvnJKCg+gh9r7ZC3geBQX+/81ek8HniB40MvdK
   f38w/v3vYej1WixceCdOnjR/uXsg4XlWBHHtGpCSYp4O7U9/Atav93aLphYHUSD19UBuLjB9OvDP
   fwJz5ni7RVOHe1YEsnSp+bsS+/uBVasC67ttnOEgTrE//xmQy81zqrz6qrdbIw4+NHvB4cPA8uVA
   RATwr38BP/iBt1vkeXxoFtAvfmGeX6WvD3j88cD61i9HeI/oJUYjMG+eeQbTN98EHnnE2y3yLN4j
   CkouB15+2fx83Tqgs9O77fE2DqIXPfggkJdnnlL3iScC+xDNh2Yv0+vNE4j39pqnw1i50tst8gz+
   QNsH7NoF/PrXJxAaehQZGSGIiBhCWdnEvgBedDwMzAfcfvsJTJ/+Pvr7N6KhwbwsUKbHHcHniALY
   seMo+vsDc3rcERxEAdy8GbjT447gIApg2rTAnR53BAdRAIE8Pe4IvmoWxOhBtNOnD+Opp7R+daHC
   H98wIXAXH/MJHEQmBA4iEwIHkQmBg8iEwEFkQuAgMiFwEJkQOIhMCBxEJgQOIhMCB5EJgYPIhMBB
   ZELgIDIhcBCZECZ9O6nJZEJRUREuXryIpKQkvPXWW4iOjrYpl5SUhKioKAQHByM0NBTNzc0uNZj5
   p0nvESsrK6HVavHVV18hOzsblZWVdsvJZDLodDq0tLRwCJlDkw5idXU1SkpKAAAlJSV49913HZbl
   2wCYM5M+NBuNRsu8y3K5HEaj0W45mUyGu+++G8HBwSgtLcXq1avtlhs9g/3Y2c+Z79HpdNDpdJLL
   j3vzlFarxeXLl22Wb9y4ESUlJeju7rYsi42Nhclksinb2dmJ2bNn48qVK9BqtaiqqsKiRYusG8E3
   T/k9l7775tgxx195IZfLcfnyZcyaNQudnZ2Ij7c/Dezs2bMBAHFxcbjvvvvQ3NxsE0TGJn2OWFhY
   iD179gAA9uzZg2XLltmU+c9//oPe7+anu379Oo4ePYrU1NTJbpL5M5qkrq4uys7OJrVaTVqtlrq7
   u4mIqKOjg/Ly8oiI6Pz586TRaEij0dD8+fNp06ZNdutyoRnMRzj7HfMN9mxK8A32zCdwEJkQOIhM
   CBxEJgQOIhMCB5EJgYPIhMBBZELgIDIhcBCZEDiITAgcRCYEDiITAgeRCYGDyITAQWRC4CAyIXAQ
   mRA4iEwIHEQmBA4iEwIHkQmBg8iEwEFkQuAgMiFwEJkQOIhMCBxEJgQOIhMCB5EJgYPIhMBBZELg
   IDIhcBCZEDiITAgcRCYEDiITAgeRCYGDyITAQWRC4CAyIXAQmRAmHcS//e1vmD9/PoKDg3H69GmH
   5err65GcnAy1Wo3NmzdPdnPMz006iKmpqXjnnXdw5513OiwzPDyM3/zmN6ivr8fZs2exf/9+fPHF
   F5PdJPNjk57BPjk52WmZ5uZmqFQqJCUlAQCKi4tx5MgRzJ07d7KbZX5q0kGUoqOjA4mJiZbXCQkJ
   aGpqslu2vLzc8jwrKwtZWVmebBrzMJ1OB51OJ7n8uEHUarW4fPmyzfJNmzahoKDAaeUymUxyQ0YH
   kfm+sTuTioqKccuPG8Rjx4651BiFQgG9Xm95rdfrkZCQ4FKdzD+55eMbRxNCL1y4EG1tbWhvb8fA
   wAAOHjyIwsJCd2yS+ZlJB/Gdd95BYmIiGhsbkZ+fj9zcXADApUuXkJ+fDwAICQnBjh07kJOTg3nz
   5qGoqIgvVJhdMhpvfvupaoRM5nCvyvyDs9+xX/asTORqzRv1eaJO0etzhoPohfo8Uafo9Tnjl0Fk
   voeDyIQgzMUK83/jRc2jXXxSCfC3wLyMD81MCBxEJgQOIhOCXwTRZDJBq9Vizpw5WLJkCXp6ehyW
   HR4eRnp6utPRQ1Lq1Ov1WLx4MebPn4+UlBRs377dpoyUEeplZWVQq9XQaDRoaWkZt13O6tu3bx80
   Gg0WLFiAO+64A62trS7VN+LTTz9FSEgIDh8+PG59k0Z+YP369bR582YiIqqsrKTnnnvOYdmtW7fS
   L3/5SyooKHC5zs7OTmppaSEiot7eXpozZw6dPXvW8v7Q0BAplUq6cOECDQwMkEajsXqfiKimpoZy
   c3OJiKixsZEyMzMdtklKfQ0NDdTT00NERHV1dS7XN1Ju8eLFlJ+fT4cOHXJYnyv8Yo9YXV2NkpIS
   AEBJSQneffddu+UMBgNqa2vx2GOPOb1Sl1LnrFmzkJaWBgCIiIjA3LlzcenSJcv7o0eoh4aGWkao
   O9pOZmYmenp6YDQa7bZJSn0///nPMWPGDEt9BoPB4c8opT4AqKqqwooVKxAXF+ewLlf5RRCNRiPk
   cjkAQC6XO/xFPvPMM9iyZQuCgpz/2FLrHNHe3o6WlhZkZmZaltkbod7R0WG1nr0yjsIjpb7R3njj
   DeTl5Tl8X2r7jhw5gjVr1gDw3Ge+QnyOKIWj0eIbN260ei2Tyez+Z7333nuIj49Henq6pR/V1TpH
   9PX1YcWKFdi2bRsiIiKs1pNi7N7Z0XoTCcHx48fx5ptv4pNPPnFYRkp9Tz/9NCorKy2jZ5wdSSbL
   Z4I43mhxuVyOy5cvY9asWejs7ER8fLxNmYaGBlRXV6O2thb9/f24du0ali9f7rBeKXUCwODgIJYv
   X44HH3wQy5Yts3pPygj1sWUMBgMUCoXdbUkd8d7a2orVq1ejvr4eMTExduuSWt+pU6dQXFwMALh6
   9Srq6uoQGhrq/gHOHjnznGLr16+nyspKIiJ68cUXx71YISLS6XR0zz33uFznrVu36KGHHqKnn37a
   bh2Dg4P0ox/9iC5cuEA3b950erFy8uTJcS8upNR38eJFUiqVdPLkyXF/Pqn1jfbwww/T22+/7bTe
   yfCLIHZ1dVF2djap1WrSarXU3d1NREQdHR2Ul5dnU16n0zm9apZS50cffUQymYw0Gg2lpaVRWloa
   1dXVWdVTW1tLc+bMIaVSSZs2bSIiotdee41ee+01S5knn3ySlEolLViwgE6dOjVuu5zVt2rVKoqN
   jbW0JyMjw6X6RvNkEIUY9MCYX1w1M9/HQWRC4CAyIXAQmRA4iEwIHEQmhP8HN5Na3YN0RYEAAAAA
   SUVORK5CYII=
   "></img>
   </div>
   </div>
   </div>
   </div>
   </div>
   <div class="cell border-box-sizing code_cell vbox">
   <div class="input hbox">
   <div class="prompt input_prompt">In&nbsp;[21]:</div>
   <div class="input_area box-flex1">
   <div class="highlight-ipynb"><pre class="ipynb"><span class="kn">from</span> <span class="nn">IPython.display</span> <span class="kn">import</span> <span class="n">HTML</span>
   <span class="n">h</span> <span class="o">=</span> \
   <span class="sd">&quot;&quot;&quot;</span>
   <span class="sd">&lt;video width=&quot;640&quot; height=&quot;480&quot; controls&gt;</span>
   <span class="sd">  &lt;source src=&quot;files/open-loop.ogv&quot; type=&quot;video/ogg&quot;&gt;</span>
   <span class="sd">  &lt;source src=&quot;files/open-loop.mp4&quot; type=&quot;video/mp4&quot;&gt;</span>
   <span class="sd">Your browser does not support the video tag, check out the YouTuve version instead: http://youtu.be/Nj3_npq7MZI.</span>
   <span class="sd">&lt;/video&gt;</span>
   <span class="sd">&quot;&quot;&quot;</span>
   <span class="n">HTML</span><span class="p">(</span><span class="n">h</span><span class="p">)</span>
   </pre></div>

   </div>
   </div>
   <div class="vbox output_wrapper">
   <div class="output vbox">
   <div class="hbox output_area">
   <div class="prompt output_prompt">Out[21]:</div>
   <div class="output_subarea output_pyout output_html rendered_html">

   <video width="640" height="480" controls>
     <source src="https://moorepants.s3.us-east-005.dream.io/open-loop.ogv" type="video/ogg">
     <source src="https://moorepants.s3.us-east-005.dream.io/open-loop.mp4" type="video/mp4">
   Your browser does not support the video tag.
   </video>

   </div>
   </div>
   </div>
   </div>
   </div>
   <div class="text_cell_render border-box-sizing rendered_html">
   <h1 class="ipynb">Controller Design</h1>
   <p>The n-link pendulum can be balanced such that all of the links are inverted above the cart by applying the correct lateral force to the cart. We can design a full state feedback controller based off of a linear model of the pendulum about its upright equilibrium point. We'll start by specifying the equilibrium point and parameters in dictionaries.</p>
   </div>
   <div class="cell border-box-sizing code_cell vbox">
   <div class="input hbox">
   <div class="prompt input_prompt">In&nbsp;[22]:</div>
   <div class="input_area box-flex1">
   <div class="highlight-ipynb"><pre class="ipynb"><span class="n">equilibrium_point</span> <span class="o">=</span> <span class="n">hstack</span><span class="p">((</span> <span class="mi">0</span><span class="p">,</span> <span class="n">pi</span> <span class="o">/</span> <span class="mi">2</span> <span class="o">*</span> <span class="n">ones</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">q</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span><span class="p">),</span> <span class="n">zeros</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">u</span><span class="p">))</span> <span class="p">))</span>
   <span class="n">equilibrium_dict</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">(</span><span class="nb">zip</span><span class="p">(</span><span class="n">q</span> <span class="o">+</span> <span class="n">u</span><span class="p">,</span> <span class="n">equilibrium_point</span><span class="p">))</span>
   <span class="n">parameter_dict</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">(</span><span class="nb">zip</span><span class="p">(</span><span class="n">parameters</span><span class="p">,</span> <span class="n">parameter_vals</span><span class="p">))</span>
   </pre></div>

   </div>
   </div>
   </div>
   <div class="text_cell_render border-box-sizing rendered_html">
   <p>The <code>KanesMethod</code> class has method that linearizes the forcing vector about generic state and input perturbation vectors. The equilibrium point and numerical constants can then be substituted in to give the linear system in this form: $M\dot{x}=F_Ax+F_Bu$. The state and input matrices, $A$ and $B$, can then be computed by left side multiplication by the inverse of the mass matrix: $A=M^{-1}F_A$ and $B=M^{-1}F_B$.</p>
   </div>
   <div class="cell border-box-sizing code_cell vbox">
   <div class="input hbox">
   <div class="prompt input_prompt">In&nbsp;[23]:</div>
   <div class="input_area box-flex1">
   <div class="highlight-ipynb"><pre class="ipynb"><span class="c"># symbolically linearize about arbitrary equilibrium</span>
   <span class="n">linear_state_matrix</span><span class="p">,</span> <span class="n">linear_input_matrix</span><span class="p">,</span> <span class="n">inputs</span> <span class="o">=</span> <span class="n">kane</span><span class="o">.</span><span class="n">linearize</span><span class="p">()</span>
   <span class="c"># sub in the equilibrium point and the parameters</span>
   <span class="n">f_A_lin</span> <span class="o">=</span> <span class="n">linear_state_matrix</span><span class="o">.</span><span class="n">subs</span><span class="p">(</span><span class="n">parameter_dict</span><span class="p">)</span><span class="o">.</span><span class="n">subs</span><span class="p">(</span><span class="n">equilibrium_dict</span><span class="p">)</span>
   <span class="n">f_B_lin</span> <span class="o">=</span> <span class="n">linear_input_matrix</span><span class="o">.</span><span class="n">subs</span><span class="p">(</span><span class="n">parameter_dict</span><span class="p">)</span><span class="o">.</span><span class="n">subs</span><span class="p">(</span><span class="n">equilibrium_dict</span><span class="p">)</span>
   <span class="n">m_mat</span> <span class="o">=</span> <span class="n">kane</span><span class="o">.</span><span class="n">mass_matrix_full</span><span class="o">.</span><span class="n">subs</span><span class="p">(</span><span class="n">parameter_dict</span><span class="p">)</span><span class="o">.</span><span class="n">subs</span><span class="p">(</span><span class="n">equilibrium_dict</span><span class="p">)</span>
   <span class="c"># compute A and B</span>
   <span class="kn">from</span> <span class="nn">numpy</span> <span class="kn">import</span> <span class="n">matrix</span>
   <span class="n">A</span> <span class="o">=</span> <span class="n">matrix</span><span class="p">(</span><span class="n">m_mat</span><span class="o">.</span><span class="n">inv</span><span class="p">()</span> <span class="o">*</span> <span class="n">f_A_lin</span><span class="p">)</span>
   <span class="n">B</span> <span class="o">=</span> <span class="n">matrix</span><span class="p">(</span><span class="n">m_mat</span><span class="o">.</span><span class="n">inv</span><span class="p">()</span> <span class="o">*</span> <span class="n">f_B_lin</span><span class="p">)</span>
   </pre></div>

   </div>
   </div>
   </div>
   <div class="text_cell_render border-box-sizing rendered_html">
   <p>Now that we have a linear system, the python-control package can be used to design an optimal controller for the system.</p>
   </div>
   <div class="cell border-box-sizing code_cell vbox">
   <div class="input hbox">
   <div class="prompt input_prompt">In&nbsp;[24]:</div>
   <div class="input_area box-flex1">
   <div class="highlight-ipynb"><pre class="ipynb"><span class="kn">import</span> <span class="nn">control</span>
   <span class="kn">from</span> <span class="nn">numpy</span> <span class="kn">import</span> <span class="n">dot</span><span class="p">,</span> <span class="n">rank</span>
   <span class="kn">from</span> <span class="nn">numpy.linalg</span> <span class="kn">import</span> <span class="n">matrix_rank</span>
   </pre></div>

   </div>
   </div>
   </div>
   <div class="text_cell_render border-box-sizing rendered_html">
   <p>First we can check to see if the system is, in fact, controllable.</p>
   </div>
   <div class="cell border-box-sizing code_cell vbox">
   <div class="input hbox">
   <div class="prompt input_prompt">In&nbsp;[25]:</div>
   <div class="input_area box-flex1">
   <div class="highlight-ipynb"><pre class="ipynb"><span class="k">assert</span> <span class="n">matrix_rank</span><span class="p">(</span><span class="n">control</span><span class="o">.</span><span class="n">ctrb</span><span class="p">(</span><span class="n">A</span><span class="p">,</span> <span class="n">B</span><span class="p">))</span> <span class="o">==</span> <span class="n">A</span><span class="o">.</span><span class="n">shape</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
   </pre></div>

   </div>
   </div>
   </div>
   <div class="text_cell_render border-box-sizing rendered_html">
   <p>The control matrix is full rank, so now we can compute the optimal gains with a linear quadratic regulator. I chose identity matrices for the weightings for simplicity.</p>
   </div>
   <div class="cell border-box-sizing code_cell vbox">
   <div class="input hbox">
   <div class="prompt input_prompt">In&nbsp;[26]:</div>
   <div class="input_area box-flex1">
   <div class="highlight-ipynb"><pre class="ipynb"><span class="n">K</span><span class="p">,</span> <span class="n">X</span><span class="p">,</span> <span class="n">E</span> <span class="o">=</span> <span class="n">control</span><span class="o">.</span><span class="n">lqr</span><span class="p">(</span><span class="n">A</span><span class="p">,</span> <span class="n">B</span><span class="p">,</span> <span class="n">ones</span><span class="p">(</span><span class="n">A</span><span class="o">.</span><span class="n">shape</span><span class="p">),</span> <span class="mi">1</span><span class="p">);</span>
   </pre></div>

   </div>
   </div>
   </div>
   <div class="text_cell_render border-box-sizing rendered_html">
   <p>The gains can now be used to define the required input during simulation to stabilize the system. The input $u$ is simply the gain vector multiplied by the error in the state vector from the equilibrium point, $u(t)=K(x_{eq} - x(t))$.</p>
   </div>
   <div class="cell border-box-sizing code_cell vbox">
   <div class="input hbox">
   <div class="prompt input_prompt">In&nbsp;[27]:</div>
   <div class="input_area box-flex1">
   <div class="highlight-ipynb"><pre class="ipynb"><span class="k">def</span> <span class="nf">right_hand_side</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">t</span><span class="p">,</span> <span class="n">args</span><span class="p">):</span>
       <span class="sd">&quot;&quot;&quot;Returns the derivatives of the states.</span>

   <span class="sd">    Parameters</span>
   <span class="sd">    ----------</span>
   <span class="sd">    x : ndarray, shape(2 * (n + 1))</span>
   <span class="sd">        The current state vector.</span>
   <span class="sd">    t : float</span>
   <span class="sd">        The current time.</span>
   <span class="sd">    args : ndarray</span>
   <span class="sd">        The constants.</span>

   <span class="sd">    Returns</span>
   <span class="sd">    -------</span>
   <span class="sd">    dx : ndarray, shape(2 * (n + 1))</span>
   <span class="sd">        The derivative of the state.</span>
   <span class="sd">    </span>
   <span class="sd">    &quot;&quot;&quot;</span>
       <span class="n">u</span> <span class="o">=</span> <span class="n">dot</span><span class="p">(</span><span class="n">K</span><span class="p">,</span> <span class="n">equilibrium_point</span> <span class="o">-</span> <span class="n">x</span><span class="p">)</span>    <span class="c"># The controller     </span>
       <span class="n">arguments</span> <span class="o">=</span> <span class="n">hstack</span><span class="p">((</span><span class="n">x</span><span class="p">,</span> <span class="n">u</span><span class="p">,</span> <span class="n">args</span><span class="p">))</span>     <span class="c"># States, input, and parameters</span>
       <span class="n">dx</span> <span class="o">=</span> <span class="n">array</span><span class="p">(</span><span class="n">solve</span><span class="p">(</span><span class="n">M_func</span><span class="p">(</span><span class="o">*</span><span class="n">arguments</span><span class="p">),</span> <span class="c"># Solving for the derivatives</span>
           <span class="n">F_func</span><span class="p">(</span><span class="o">*</span><span class="n">arguments</span><span class="p">)))</span><span class="o">.</span><span class="n">T</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>

       <span class="k">return</span> <span class="n">dx</span>
   </pre></div>

   </div>
   </div>
   </div>
   <div class="text_cell_render border-box-sizing rendered_html">
   <p>Now we can simulate and animate the system to see if the controller works.</p>
   </div>
   <div class="cell border-box-sizing code_cell vbox">
   <div class="input hbox">
   <div class="prompt input_prompt">In&nbsp;[28]:</div>
   <div class="input_area box-flex1">
   <div class="highlight-ipynb"><pre class="ipynb"><span class="n">x0</span> <span class="o">=</span> <span class="n">hstack</span><span class="p">((</span> <span class="mi">0</span><span class="p">,</span> <span class="n">pi</span> <span class="o">/</span> <span class="mi">2</span> <span class="o">*</span> <span class="n">ones</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">q</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span><span class="p">),</span> <span class="mi">1</span> <span class="o">*</span> <span class="n">ones</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">u</span><span class="p">))</span> <span class="p">))</span> <span class="c"># Initial conditions, q and u</span>
   <span class="n">t</span> <span class="o">=</span> <span class="n">linspace</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">10</span><span class="p">,</span> <span class="mi">1000</span><span class="p">)</span>                                       <span class="c"># Time vector</span>
   <span class="n">y</span> <span class="o">=</span> <span class="n">odeint</span><span class="p">(</span><span class="n">right_hand_side</span><span class="p">,</span> <span class="n">x0</span><span class="p">,</span> <span class="n">t</span><span class="p">,</span> <span class="n">args</span><span class="o">=</span><span class="p">(</span><span class="n">parameter_vals</span><span class="p">,))</span>      <span class="c"># Actual integration</span>
   </pre></div>

   </div>
   </div>
   </div>
   <div class="text_cell_render border-box-sizing rendered_html">
   <p>The plots show that we seem to have a stable system.</p>
   </div>
   <div class="cell border-box-sizing code_cell vbox">
   <div class="input hbox">
   <div class="prompt input_prompt">In&nbsp;[29]:</div>
   <div class="input_area box-flex1">
   <div class="highlight-ipynb"><pre class="ipynb"><span class="n">lines</span> <span class="o">=</span> <span class="n">plot</span><span class="p">(</span><span class="n">t</span><span class="p">,</span> <span class="n">y</span><span class="p">[:,</span> <span class="p">:</span><span class="n">y</span><span class="o">.</span><span class="n">shape</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="o">/</span> <span class="mi">2</span><span class="p">])</span>
   <span class="n">lab</span> <span class="o">=</span> <span class="n">xlabel</span><span class="p">(</span><span class="s">&#39;Time [sec]&#39;</span><span class="p">)</span>
   <span class="n">leg</span> <span class="o">=</span> <span class="n">legend</span><span class="p">(</span><span class="n">dynamic</span><span class="p">[:</span><span class="n">y</span><span class="o">.</span><span class="n">shape</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="o">/</span> <span class="mi">2</span><span class="p">])</span>
   </pre></div>

   </div>
   </div>
   <div class="vbox output_wrapper">
   <div class="output vbox">
   <div class="hbox output_area">
   <div class="prompt output_prompt"></div>
   <div class="output_subarea output_display_data">
   <img src="data:image/png;base64,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
   E1HXOIlHAAAAAElFTkSuQmCC
   "></img>
   </div>
   </div>
   </div>
   </div>
   </div>
   <div class="cell border-box-sizing code_cell vbox">
   <div class="input hbox">
   <div class="prompt input_prompt">In&nbsp;[30]:</div>
   <div class="input_area box-flex1">
   <div class="highlight-ipynb"><pre class="ipynb"><span class="n">lines</span> <span class="o">=</span> <span class="n">plot</span><span class="p">(</span><span class="n">t</span><span class="p">,</span> <span class="n">y</span><span class="p">[:,</span> <span class="n">y</span><span class="o">.</span><span class="n">shape</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="o">/</span> <span class="mi">2</span><span class="p">:])</span>
   <span class="n">lab</span> <span class="o">=</span> <span class="n">xlabel</span><span class="p">(</span><span class="s">&#39;Time [sec]&#39;</span><span class="p">)</span>
   <span class="n">leg</span> <span class="o">=</span> <span class="n">legend</span><span class="p">(</span><span class="n">dynamic</span><span class="p">[</span><span class="n">y</span><span class="o">.</span><span class="n">shape</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="o">/</span> <span class="mi">2</span><span class="p">:])</span>
   </pre></div>

   </div>
   </div>
   <div class="vbox output_wrapper">
   <div class="output vbox">
   <div class="hbox output_area">
   <div class="prompt output_prompt"></div>
   <div class="output_subarea output_display_data">
   <img src="data:image/png;base64,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
   "></img>
   </div>
   </div>
   </div>
   </div>
   </div>
   <div class="cell border-box-sizing code_cell vbox">
   <div class="input hbox">
   <div class="prompt input_prompt">In&nbsp;[31]:</div>
   <div class="input_area box-flex1">
   <div class="highlight-ipynb"><pre class="ipynb"><span class="n">animate_pendulum</span><span class="p">(</span><span class="n">t</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">arm_length</span><span class="p">,</span> <span class="n">filename</span><span class="o">=</span><span class="s">&quot;closed-loop.ogv&quot;</span><span class="p">)</span>
   <span class="n">animate_pendulum</span><span class="p">(</span><span class="n">t</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">arm_length</span><span class="p">,</span> <span class="n">filename</span><span class="o">=</span><span class="s">&quot;closed-loop.mp4&quot;</span><span class="p">)</span>
   </pre></div>

   </div>
   </div>
   <div class="vbox output_wrapper">
   <div class="output vbox">
   <div class="hbox output_area">
   <div class="prompt output_prompt"></div>
   <div class="output_subarea output_display_data">
   <img src="data:image/png;base64,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
   "></img>
   </div>
   </div>
   <div class="hbox output_area">
   <div class="prompt output_prompt"></div>
   <div class="output_subarea output_display_data">
   <img src="data:image/png;base64,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
   "></img>
   </div>
   </div>
   </div>
   </div>
   </div>
   <div class="cell border-box-sizing code_cell vbox">
   <div class="input hbox">
   <div class="prompt input_prompt">In&nbsp;[32]:</div>
   <div class="input_area box-flex1">
   <div class="highlight-ipynb"><pre class="ipynb"><span class="kn">from</span> <span class="nn">IPython.display</span> <span class="kn">import</span> <span class="n">HTML</span>
   <span class="n">h</span> <span class="o">=</span> \
   <span class="sd">&quot;&quot;&quot;</span>
   <span class="sd">&lt;video width=&quot;640&quot; height=&quot;480&quot; controls&gt;</span>
   <span class="sd">  &lt;source src=&quot;files/closed-loop.ogv&quot; type=&quot;video/ogg&quot;&gt;</span>
   <span class="sd">  &lt;source src=&quot;files/closed-loop.mp4&quot; type=&quot;video/mp4&quot;&gt;</span>
   <span class="sd">Your browser does not support the video tag, check out the YouTube version instead: http://youtu.be/SpgBHqW9om0</span>
   <span class="sd">&lt;/video&gt;</span>
   <span class="sd">&quot;&quot;&quot;</span>
   <span class="n">HTML</span><span class="p">(</span><span class="n">h</span><span class="p">)</span>
   </pre></div>

   </div>
   </div>
   <div class="vbox output_wrapper">
   <div class="output vbox">
   <div class="hbox output_area">
   <div class="prompt output_prompt">Out[32]:</div>
   <div class="output_subarea output_pyout output_html rendered_html">

   <video width="640" height="480" controls>
     <source src="https://moorepants.s3.us-east-005.dream.io/closed-loop.ogv" type="video/ogg">
     <source src="https://moorepants.s3.us-east-005.dream.io/closed-loop.mp4" type="video/mp4">
   Your browser does not support the video tag.
   </video>

   </div>
   </div>
   </div>
   </div>
   </div>
   <div class="text_cell_render border-box-sizing rendered_html">
   <p>The video clearly shows that our controller can balance all $n$ of the pendulum links. The weightings in the lqr design can be tweaked to give different performance if needed.</p>
   <p>This example shows that the free and open source scientific Python tools for dynamics are easily comparable in ability and quality a commercial package such as Mathematica. Besides the current installation hurdles for Python, I'd like to claim that it may better than commercial packages, due to our much more robust SymPy <strong>mechanics</strong> package and the fact that all of the code is liberally licensed for reuse and hacking.</p>
   <p>The IPython notebook for this example can be downloaded from https://github.com/gilbertgede/idetc-2013-paper/blob/master/n-pendulum-control.ipynb. Yo ucan try out different $n$ values. I've gotten the equations of motion to compute and an open loop simulation of 10 links. My computer ran out of memory when I tried to compute for $n=50$. The controller weightings and initial conditions will probably have to be adjusted for better performance for $n&gt;5$, but it should work. Let me know the resuls if you play with it.</p>
   </div>
   </div>
