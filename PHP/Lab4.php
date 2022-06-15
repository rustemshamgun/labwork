<?php

<?php
    $a = 100;
    $result = $a >= 5 && $a < 10 || $a == 100;

    // 1. Сначала подставляем значения
    $result = 100 >= 5 && 100 < 10 || 100 == 100;

    // 2. Затем выполняем операторы сравнения, получаем:
    $result = true && false || true;

    // 3. true && false возвращает false.
    $result = false || true;

    // 4. false || true возвращает true
?>