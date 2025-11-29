// Переменные для контроля
const totalRepeats = 3;
let currentRepeat = 0;
let allTimes = []; // массив всех времен для финальной статистики

// Функция для запуска следующего раунда
function startNextRepeat() {
  if (currentRepeat >= totalRepeats) {
    // Все три повторения завершены - выводим статистику
    showFinalStatistics();
    return;
  }
  currentRepeat++;
  runTestRound(() => {
    // после завершения каждого раунда
    startNextRepeat();
  });
}

// Основная функция для запуска одного тестового раунда
function runTestRound(callback) {
  // Вам нужно заменить или встроить сюда ваш существующий код запуска теста
  // Например, вот как выглядел бы пример, основанный на моем предыдущем ответ:
  // Предположим, что у вас есть функция runSingleTest(callback)
  runSingleTest(callback);
}

// Функция, которая запускает один тест
function runSingleTest(onComplete) {
  // Тут должен быть ваш существующий код, который по завершении
  // добавляет время в массив allTimes и вызывает onComplete
  // Например:
  let shuffledNumbers = shuffleArray([...numbers]);
  let index = 0;
  let startTime = 0;

  // Здесь вставьте ваш существующий цикл/логику, чтобы измерять время:
  // Например:
  // показывать числа, ждать нажатия, измерять время
  // После завершения раунда, добавьте результат:
  // allTimes.push(время);
  // then вызовите onComplete();
  // Предположим, что ваш код уже делает это, и вы просто вызываете onComplete() после
  // окончания тестового раунда.

  // Общий пример (замените на ваш код):
  // Для демонстрации — вызовите onComplete() сразу
  // с имитацией времени, например:
  const simulatedTime = Math.floor(Math.random() * 200 + 1); // случайное время
  allTimes.push(simulatedTime);
  // вызовите onComplete после окончания теста
  onComplete();
}

// Функция для отображения итоговой статистики
function showFinalStatistics() {
  const sum = allTimes.reduce((a, b) => a + b, 0);
  const avg = (sum / allTimes.length).toFixed(2);
  const averageTime = parseFloat(avg);

  // определение интерпретации
  let interpretation = '';
  if (averageTime <= 15) {
    interpretation = "Невероятный ингибиторный контроль. Вы невероятны.";
  } else if (averageTime <= 25) {
    interpretation = "Отличный ингибиторный контроль. Вы выше нормы.";
  } else if (averageTime <= 35) {
    interpretation = "Хороший ингибиторный контроль.";
  } else if (averageTime <= 60) {
    interpretation = "Нормальный ингибиторный контроль.";
  } else if (averageTime <= 100) {
    interpretation = "Плохой ингибиторный контроль. Вам надо развиваться.";
  } else {
    interpretation = "Очень плохой ингибиторный контроль. Вам срочно надо развиваться.";
  }

  // Выводим статистику в HTML
  document.getElementById('test-area').style.display = 'none';
  document.getElementById('final-stats').style.display = 'block';
  document.getElementById('final-stats').innerHTML = `
    <h3>Результаты после ${totalRepeats} повторений:</h3>
    <p>Среднее время: <b>${avg}</b> секунд</p>
    <p>Интерпретация: ${interpretation}</p>
    <p>Все результаты: ${allTimes.join(', ')} секунд</p>
  `;
  // Также можете вывести здесь итог в любом другом месте
  document.getElementById('results-summary').innerHTML = `Среднее время: <b>${avg}</b> секунд. ${interpretation}`;
}

// Ваша кнопка запуска
document.getElementById('start-test-btn').onclick = () => {
  // Сброс данных
  allTimes = [];
  currentRepeat = 0;
  // Запускаем последовательность повторений
  startNextRepeat();
};
table.classList.remove('blured');
JSON.parse(localStorage.getItem(key)) || [];