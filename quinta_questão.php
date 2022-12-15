<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <style>
    </style>
  </head>
  <body>
    <div class="invertido">
      <form class="" method="post">
        <input type="text" name="inversao">
      </form>
    </div>
    <?php
      $texto = $_POST['inversao'];
      echo strrev($texto);
    ?>
  </body>
</html>
