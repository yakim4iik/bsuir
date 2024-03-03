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

function getValidInputData() {
	let inputPairFirstElem = document
		.getElementById('InputPairFirstElem')
		.value.replace(/\s+/g, '')
	let inputPairSecondElem = document
		.getElementById('InputPairSecondElem')
		.value.replace(/\s+/g, '')
	inputPairFirstElem = inputPairFirstElem.replace(/,+$/g, '')
	inputPairSecondElem = inputPairSecondElem.replace(/,+$/g, '')

	if (!inputPairFirstElem.length || !inputPairSecondElem.length) {
		displayErrorMessage('Одно из полей пусто')
		return
	}

	let nums1 = inputPairFirstElem.split(',')
	let nums2 = inputPairSecondElem.split(',')

	if (nums1.length !== nums2.length) {
		displayErrorMessage('Векторы не совпадают по длине')
		return
	}

	for (let i = 0; i < nums1.length; i++) {
		if (!isNum(nums1[i]) || !isNum(nums2[i])) {
			displayErrorMessage('Встречен неопознанный символ')
			return
		}
	}

	let resNums1 = []
	let resNums2 = []

	for (let i = 0; i < nums1.length; i++) {
		let temp = parseInt(nums1[i])
		if (temp > 15) {
			displayErrorMessage('Ошибка: введенное число ' + temp + ' больше 15')
			return
		}
		resNums1.push(convertDecToBin(temp))
	}

	for (let i = 0; i < nums2.length; i++) {
		let temp = parseInt(nums2[i])
		if (temp > 15) {
			displayErrorMessage('Ошибка: введенное число ' + temp + ' больше 15')
			return
		}
		resNums2.push(convertDecToBin(temp))
	}

	hideErrorMessage()

	document.getElementById('InputVector1').innerHTML =
		'Вектор №1 = (' + nums1 + ')'
	document.getElementById('InputVector2').innerHTML =
		'Вектор №2 = (' + nums2 + ')'

	return [resNums1, resNums2]
}

function isNum(inNum) {
	return /^\d+$/.test(inNum)
}

function convertDecToBin(number) {
	return (number >>> 0)
		.toString(2)
		.padStart(MACHINE_WORD, '0')
		.split('')
		.map(Number)
}

function displayErrorMessage(message) {
	let errorMessage = document.getElementById('ErrorMas')
	errorMessage.innerHTML = message
	errorMessage.style.display = 'block'
}

function hideErrorMessage() {
	let errorMessage = document.getElementById('ErrorMas')
	errorMessage.style.display = 'none'
}

function getNums() {
	let testData = getValidInputData()
	return testData
}
