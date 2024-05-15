//////////////////////////////////////////////////////////////////////////////////////
// Лабораторная работа 2 по дисциплине МРЗвИС
// Выполнена студентами группы 121703
// БГУИР Титлов И.Д., Якимович И.В.
// Вариант 14
// 13.05.2024
//Методы для работы с DOM взяты из ресурса: http://learn.javascript.ru/document
//Метод генерации случайных значение взят из источника http://javascript.ru/math.random
//Методы для создания таблицы взяты из ресурса: https://www.w3schools.com/jsref/coll_table_rows.asp

var timeSum = 0
var timeDiff = 0
var timeMult = 0
var timeDiv = 0
var timeCompare = 0
var countSum = 0
var countDiff = 0
var countMult = 0
var countDiv = 0
var countCompare = 0

var countF = 0
var countD = 0
var countImplicationAB = 0
var countImplicationBA = 0
var countMaxFD = 0

var rang = 0
var T1 = 0
var Tn = 0
var Ky = 0
var e = 0
var D = 0
var Lsum = 0
var Lavg = 0

var matrixA
var matrixB
var matrixE
var matrixG
var matrixC
var f
var d
var m
var p
var q
var n

function main() {
	// Получение введенных пользователем значений
	m = +document.getElementById('m').value
	p = +document.getElementById('p').value
	q = +document.getElementById('q').value
	n = +document.getElementById('n').value
	timeSum = +document.getElementById('sum').value
	timeDiff = +document.getElementById('dif').value
	timeMult = +document.getElementById('mul').value
	timeCompare = +document.getElementById('com').value
	timeDiv = +document.getElementById('div').value
	// Генерация матрицы значеними, в зависимости от размерности p, m, q
	matrixA = setMatrix(p, m)
	matrixB = setMatrix(m, q)
	matrixE = setMatrix(1, m)
	matrixG = setMatrix(p, q)
	// Вывод данных матрицы в таблицу
	fillTable(matrixA, p, m, 'a')
	fillTable(matrixB, m, q, 'b')
	fillTable(matrixE, 1, m, 'e')
	fillTable(matrixG, p, q, 'g')

	d = executeD() // dijk
	console.log(d)
	f = executeF() // fijk
	console.log(f)
	matrixC = executeC() //  cij
	fillTable(matrixC, p, q, 'c')

	T1 =
		timeSum * countSum +
		timeDiff * countDiff +
		timeMult * countMult +
		timeDiv * countDiv +
		timeCompare * countCompare
	Lsum = Tn
	Ky = T1 / Tn
	e = Ky / n
	rang = p * q * m
	Lavg += (7 * timeMult + 2 * timeSum + 3 * timeDiff) * p * q // C
	Lavg += (7 * timeMult + 2 * timeSum + 3 * timeDiff) * rang // F
	Lavg += timeMult * rang // D
	Lavg += timeMult * (m - 1) * countF //~f
	Lavg += (timeDiff * (m + 1) + timeMult * (m - 1)) * countD // ~d
	Lavg += (timeDiff + timeSum + timeCompare) * countMaxFD // max f d
	Lavg += (timeDiv + timeDiff) * countImplicationAB // a->b
	Lavg += (timeDiv + timeDiff) * countImplicationBA // b->a
	Lavg /= rang
	D = Lsum / Lavg

	var operationData = [
		['Sum', 'Difference', 'Multiplicity', 'Division', 'Comparing'],
		[
			timeSum * countSum,
			timeDiff * countDiff,
			timeMult * countMult,
			timeDiv * countDiv,
			timeCompare * countCompare,
		],
	]
	fillTable(operationData, 2, 5, 'operationData')

	var executedData = [
		['T1', 'Tn', 'Ky', 'e', 'D', 'Lavg', 'Lsum'],
		[T1, Tn, Ky, e, D, Lavg, Lsum],
	]
	fillTable(executedData, 2, 7, 'executedData')
}
// Генерация матрицы значениями [-1; 1]
function setMatrix(rows, columns) {
	var matrix = []
	for (var row = 0; row < rows; row++) {
		matrix[row] = []
		for (var column = 0; column < columns; column++) {
			matrix[row][column] = Math.random() * (1 + 1) - 1
		}
	}
	return matrix
}
// Заполнение таблицы сгенерированными значениями
function fillTable(data, rows, columns, tableName) {
	var table = document.getElementById(tableName)
	// Очистка таблицы перед заполнением
	while (table.firstChild) {
		table.firstChild.remove()
	}
	for (var row = 0; row < rows; row++) {
		table.insertRow(-1)
		for (var column = 0; column < columns; column++) {
			table.rows[row].insertCell(-1)
			table.rows[row].cells[column].innerText = data[row][column]
		}
	}
}

function executeC() {
	var cij = []
	var operationTime = 0
	for (var i = 0; i < p; i++) {
		cij[i] = []
		for (var j = 0; j < q; j++) {
			cij[i][j] =
				notAndF(i, j) * (3 * matrixG[i][j] - 2) * matrixG[i][j] +
				(notOrD(i, j) +
					(4 * maxFandD(i, j) - 3 * notOrD(i, j)) * matrixG[i][j]) *
					(1 - matrixG[i][j])
			console.log(cij[i][j])
			countMult += 7
			countDiff += 3
			countSum += 2
		}
	}

	operationTime =
		(7 * timeMult +
			3 * timeSum +
			4 * timeDiff +
			2 * (m - 1) * timeMult +
			3 * (timeDiff * (m + 1) + timeMult * (m - 1)) +
			timeCompare) *
		Math.ceil((p * q) / n)
	Tn += operationTime
	return cij
}
function deltaCalculation(a, b) {
	countDiff++
	countSum++
	countCompare += 2
	countImplicationAB++

	var result = Math.max(1 - a + b, 0)
	return Math.min(result, 1)
}

function executeF() {
	var fijk = []
	var operationTime = 0
	for (var i = 0; i < p; i++) {
		fijk[i] = []
		for (var j = 0; j < q; j++) {
			fijk[i][j] = []
			for (var k = 0; k < m; k++) {
				fijk[i][j][k] =
					deltaCalculation(matrixA[i][k], matrixB[k][j]) *
						(2 * matrixE[0][k] - 1) *
						matrixE[0][k] +
					deltaCalculation(matrixB[k][j], matrixA[i][k]) *
						(1 +
							(4 * deltaCalculation(matrixA[i][k], matrixB[k][j]) - 2) *
								matrixE[0][k]) *
						(1 - matrixE[0][k])
				countMult += 7
				countDiff += 3
				countSum += 2
			}
		}
	}
	operationTime =
		(7 * timeMult + 2 * timeSum + 6 * timeDiff + 3 * timeDiv) *
		Math.ceil((p * q * m) / n)
	Tn += operationTime
	return fijk
}

function executeD() {
	var dijk = []
	var operationTime = 0
	for (var i = 0; i < p; i++) {
		dijk[i] = []
		for (var j = 0; j < q; j++) {
			dijk[i][j] = []
			for (var k = 0; k < m; k++) {
				var result = matrixA[i][k] + matrixB[k][j] - 1.0
				dijk[i][j][k] = Math.max(result, 0.0)
				countSum += 2
				countDiff++
				countCompare++
			}
		}
	}
	operationTime = timeMult * Math.ceil((p * q * m) / n)
	Tn += operationTime
	return dijk
}

function notAndF(i, j) {
	var result = 1
	for (var k = 0; k < m; k++) {
		result *= f[i][j][k]
	}
	console.log(result)
	countF++
	countMult += m - 1
	return result
}

function notOrD(i, j) {
	var result = 1
	for (var k = 0; k < m; k++) {
		result *= 1 - d[i][j][k]
	}
	console.log(result)
	countD++
	countMult += m - 1
	countDiff += m + 1
	return 1 - result
}

function maxFandD(i, j) {
	var result = 0
	result = i * j
	console.log(result)
	countMult++
	return result
}
