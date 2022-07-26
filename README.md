<h1>HaarClassifier</h1>
<h2>Table of Contents</h2>
<ul>
  <li><a href=#porpuse>Porpuse</a></li>
  <li><a href=#introduction>Introduction</a></li>
  <li><a href=#data>Data</a></li>
  <li><a href=#model>Model</a></li>
  <li><a href=#tutorial>Tutorial</a>
    <ul>
      <li><a href=#opencv_createsamples>opencv_createsamples</a></li>
      <li><a href=#opencv_traincascade>opencv_traincascade</a></li>
      <li><a href=#xmlfiles>XML Files</a></li>
      <li><a href=#python>Python</a></li>
      <li><a href=#environment>Environment</a></li>
    </ul>
  </li>
  <li><a href=#>Futute Studies</a>
  <li><a href=#>How to run the software</a>

</ul>
<h2>Porpuse</h2>
<p>This software is designed for this purpose to be a tool to use haar cascade based on opencv to detect images with minimum inputes.</p>

<h2>Introduction</h2>
<p>According to .</p>
<p>Therefore, analyzing and comparing .</p>
<p>HaarClassifier software which is a teamwork project for <a href='https://dibris.unige.it/en'>'Dipartimento di Informatica, Bioingegneria, Robotica e Ingegneria dei Sistemi'</a> course from the prestigious master program of <a href='http://www.itim.unige.it/cs/strategos/'>'Engineering Technology for Strategy and Security - Strategos'</a> at the <a href='https://unige.it/en'>University of Genova</a> is designed to model this scenario.</p>

<h2>Data</h2>
<p>These images are .... .</p>
<p>These images are .... .</p>
<h3>Input Images</h3>
<ul>
  <li>Neg_images</li>
  <li>Pos_images</li>
</ul>

<h2>Model</h2>
<p>This model currently evaluating, analyzing, and comparing .</p>
<p>This model calculates <b>deterministic</b> and <b> (probabilistic)</b> AAAA.</p>
<h3>Input Deterministic Parameters</h3>
<ul>
  <li>Dis</li>
  <li>Ave</li>
  <li>Ves</li>
  <li>Ves</li>
</ul>

<p>All  outputs.</p>
<p>The  pictures.</p>
<figure>
<p>In this picture you can see .</p>
<img src="https://github.com" alt="TT">
</figure><br>
<figure>
<p>And in this one you see how .</p>
<img src="https://github.com/" alt="CC">
</figure>

<h2>Tutorial</h2>
<h3>Data</h3>
<p>1 - At the first you should .</p>
<p>2 - Define one </p>
<p>3 - In this step, from <a href='https://www.'>..... website</a> and compared  <a href='https://www'>.... website</a>. You can also change .</p>
<p>4 - The software recommends you .</p>
<p>Finally, .</p>
<figure>
<img src="https://github.com/" alt="tutorial data">
</figure><br>

<h3>opencv_createsamples</h3>
<p>these commands are for image_0</p>
<p>use this command for create the samples.</p>
<pre>opencv_createsamples -img /opencv_workspace/haarclass/images/pos/image_0.jpg -bg bg.txt -info /opencv_workspace/haarclass/image_0/info/info.lst -pngoutput /opencv_workspace/haarclass/image_0/info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 3000</pre>
<p>use this command for vec file.</p>
<pre>opencv_createsamples -info /opencv_workspace/haarclass/image_0/info/info.lst -num 3000 -w 20 -h 20 -vec /opencv_workspace/haarclass/image_0/positives.vec</pre>

<h3>opencv_traincascade</h3>
<p>this commands are for image_0</p>
<p>use this command for train.</p>
<pre>opencv_traincascade -data /opencv_workspace/haarclass/image_0/data -vec /opencv_workspace/haarclass/image_0/positives.vec -bg bg.txt -numPos 2600 -numNeg 1300 -numStages 10 -w 20 -h 20</pre>

<h3>XML Files</h3>
<p> .....</p>
<p>You can also.</p>
<p>6 - Based on this <a href='https://www'>reference</a>, .</p>

<h3>Python</h3>
<p>15 - You should .</p>
<p>In the .</p>
<ul>
  <li>code_1.py</li>
  <li>image_creator.py</li>
  <li>no_code.py</li>
  <li>show_time</li>
</ul>

<h3>Environment</h3>
<p>In this tab, <a href='https://www.'>this article</a>.</p>
<figure>
<img src="https://github.com/" alt="tutorial Environment">
</figure><br>