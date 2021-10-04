<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Movies</title>
</head>
<body>
  <div>
  <form action="/submit" id="userform" method="post">
  <p><strong>Title: </strong><input name="Title" placeholder="Feature Title"required/></p>
  <p><strong>Format </strong><select name="Format" placeholder="Client">
    <option value='DVD'>DVD</option>
    <option value='VHS'>VHS</option>
    <option value='STREAMING'>STREAMING</option>
  </select></p>
  <p><strong>Length: </strong><input name="Length" placeholder="Length in Minutes"required/></p>
  <p><strong>Release Year: </strong><input name="Release_Year" placeholder="Enter Year yyyy"required/></p>
  <p><strong>Rating </strong><select name="Rating"/>
    <option value= 1>1</option>
    <option value= 2>2</option>
    <option value= 3>3</option>
    <option value= 4>4</option>
    <option value= 5>5</option>
  </select></p>
  <td><input type="submit" id="submit" value="Submit" class="button"></td>
</form>
</div>
<div>
    <h2 align="center">List of Movies</h2> <BR><BR>
    <table border="0" style="width:50%; min-width:300px;" align="center">
    <tbody>
    <tr style="background:#333; color: white;">
        <th scope="col">Title</th>
        <th scope="col">Format</th>
        <th scope="col">Length</th>
        <th scope="col">Release Year</th>
        <th scope="col">Rating</th>
    </tr>
    {{!chart}}
    </tbody>
</div>
</body>
</html>
