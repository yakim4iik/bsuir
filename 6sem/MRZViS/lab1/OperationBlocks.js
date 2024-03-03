//////////////////////////////////////////////////////////////////////////////////////
// Лабораторная работа 1 по дисциплине МРЗвИС
// Выполнена студентами группы 121703
// БГУИР Титлов И.Д., Якимович И.В.
// Вариант 3 - алгоритм вычисления произведения пары 4-разрядных чисел
// умножением со старших разрядов со сдвигом множимого вправо;
// 22.02.2024
// Использованные материалы:
// https://www.w3schools.com/js/ - методические материалы по JS
// https://ru.wikipedia.org/wiki/ - описание работы конвейера
// https://habr.com/ru/post/182002/ - реализация конвейера компьютерных процессоров
// http://dit.isuct.ru/IVT/BOOKS/ARCHITECTURE/arch2/GLAVA_7.HTM - описание работы процессорного конвейера
// http://perscom.ru/2012-01-20-09-26-05/8-konveer-komand/19-konveer-komand - описание работы процессорного конвейера

function and(num1, num2) {
	RESULT.push('And')
	RESULT.push(num1)
	RESULT.push(createArray(MACHINE_WORD, num2))
	if (num2 === 1) {
		return num1
	} else {
		return createArray(MACHINE_WORD)
	}
}

function sum(num1, num2) {
	RESULT.push('Sum')
	RESULT.push(num1)
	RESULT.push(num2)
	let result = createArray(MACHINE_WORD)
	let carry = 0
	for (let i = MACHINE_WORD - 1; i >= 0; i--) {
		let sum = num1[i] + num2[i] + carry
		result[i] = sum % 2
		carry = Math.floor(sum / 2)
	}
	return result
}

function shearRight(num1, shearVal) {
	RESULT.push('ShiftRight')
	RESULT.push(num1)
	RESULT.push(convertDecToBin(shearVal))
	if (shearVal === 0) {
		return num1
	}
	let result = createArray(MACHINE_WORD)
	for (let i = shearVal; i < MACHINE_WORD; i++) {
		result[i] = num1[i - shearVal]
	}
	return result
}

function createArray(arrayLength, filler = 0) {
	return Array.from({ length: arrayLength }, () => filler)
}

function shearLeft(num1, shearVal) {
	if (shearVal === 0) return num1

	let result = createArray(MACHINE_WORD)
	for (let i = shearVal; i < MACHINE_WORD; i++) {
		result[i - shearVal] = num1[i]
	}
	return result
}
