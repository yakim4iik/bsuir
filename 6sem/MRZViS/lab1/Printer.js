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
// https://www.studytonight.com/computer-architecture/pipelining#:~:text=An%20instruction%20pipeline%20reads%20instruction,into%20segments%20of%20equal%20duration.
// https://www.javatpoint.com/instruction-pipeline

function printer(array, executionTime) {
	for (let i = 0; i < array.length; i++) {
		console.log(
			'Ответ' + i + ' - ' + convertBinToDec(array[i][array[i].length - 1])
		)
	}

	let ticsCount =
		((TICS_PER_AND_INSTRUCTION +
			TICS_PER_SHEAR_RIGHT_INSTRUCTION +
			TICS_PER_SUM_INSTRUCTION) *
			MACHINE_WORD) /
		2

	let table = document.getElementById('Table')
	while (table.rows.length !== 0) {
		while (table.rows[0].cells.length !== 0) {
			table.rows[0].deleteCell(0)
		}
		table.deleteRow(0)
	}

	for (let j = 0; j < ticsCount + array.length - 1; j++) {
		table.insertRow(-1)
		for (let k = 0; k < (MACHINE_WORD / 2) * STEPS_COUNT; k++) {
			table.rows[j].insertCell(-1)
		}
	}

	formatCellInfo(table, array)

	for (let i = 0; i < table.rows.length; i++) {
		table.rows[i].insertCell(0)
		table.rows[i].cells[0].innerText = 'такт ' + (i + 1)
	}

	table.insertRow(0)
	for (let i = 0; i < table.rows[1].cells.length; i++) {
		table.rows[0].insertCell(0)
	}

	for (let i = 1; i < table.rows[0].cells.length; i += 3) {
		table.rows[0].cells[i].innerText = 'Этап AND\n(MULTIPLICATION)'
		table.rows[0].cells[i + 1].innerText = 'Этап сдвига '
		table.rows[0].cells[i + 2].innerText = 'Этап сложения '
	}

	let res = []
	for (let i = 0; i < array.length; i++) {
		res.push(convertBinToDec(array[i][array[i].length - 1]))
	}
	document.getElementById('Answer').innerHTML =
		'Результат: (' + res.toString() + ') за время ' + executionTime + 'мс'
}

function formatCellInfo(table, array) {
	let offset = (MACHINE_WORD / 2) * STEPS_COUNT * 3
	for (let i = 0; i < array.length; i++) {
		for (let j = 0; j < array[i].length; j++) {
			table.rows[j + i].cells[j].innerText =
				RESULT[i * offset + j * 3] +
				':\n' +
				formatBinNum(RESULT[i * offset + j * 3 + 1]) +
				'\n' +
				formatBinNum(RESULT[i * offset + j * 3 + 2]) +
				'\n=' +
				formatBinNum(array[i][j])
		}
	}
}

function formatBinNum(num) {
	let result = ''
	for (let i = 0; i < MACHINE_WORD; i++) {
		if (i % 4 === 0 && i !== 0) {
			result += '-'
		}
		result += num[i]
	}
	return result
}

function convertBinToDec(number) {
	let result = 0
	for (let i = MACHINE_WORD - 1; i >= 0; i--) {
		result += number[i] * Math.pow(2, MACHINE_WORD - i - 1)
	}
	return result
}
