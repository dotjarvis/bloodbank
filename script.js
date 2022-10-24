const equals = document.querySelector(`.equals`);
const display = document.querySelector(`.display`);
const numbers = document.querySelector(`.main-calc-body`);
const operation = document.querySelector(`.main-calc-body`);

operation.addEventListener(`click`, function (e) {
  e.preventDefault();
  const operant = e.target.closest(`.operation`);
  if (!operant) return;

  const operationSignFunction = function (operantName, operantSign) {
    if (operant.classList.contains(`clear`)) display.textContent = ``;
    if (operant.classList.contains(operantName))
      display.textContent += operantSign;
  };

  operationSignFunction(`multiply`, ` x `);
  operationSignFunction(`divide`, ` / `);
  operationSignFunction(`plus`, ` + `);
  operationSignFunction(`minus`, ` - `);
});

numbers.addEventListener(`click`, function (e) {
  e.preventDefault();
  const number = e.target.closest(`.number`);
  if (!number) return;

  display.textContent += +number.textContent;
});

equals.addEventListener(`click`, function (e) {
  e.preventDefault();
  //   if ` = ` present remove it
  let displayValue = display.textContent.split(`=`);
  const valueAfterEqual =
    displayValue.length === 1 ? display.textContent : displayValue[1].trim();

  const operant = valueAfterEqual.split(` `)[1];

  let splitted;
  let finalResult;

  if (operant === `x`) {
    splitted = valueAfterEqual.split(`x`);
    finalResult = +splitted[0] * +splitted[1];
  }
  if (operant === `/`) {
    splitted = valueAfterEqual.split(`/`);
    finalResult = +splitted[0] / +splitted[1];
  }
  if (operant === `-`) {
    splitted = valueAfterEqual.split(`-`);
    finalResult = +splitted[0] - +splitted[1];
  }
  if (operant === `+`) {
    splitted = valueAfterEqual.split(`+`);
    finalResult = +splitted[0] + +splitted[1];
  }

  display.textContent = `${valueAfterEqual}  = ${finalResult}`;
});
