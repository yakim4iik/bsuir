const ALPHABET_RUS_UPPER = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
const ALPHABET_RUS_LOWER = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

function generatePassword(length) {
	const minElement = 1040
	const maxElement = 1103

	let result = ''
	for (var i = 0; i < length; i++) {
		let randomIndex =
			Math.floor(Math.random() * (maxElement - minElement + 1)) + minElement
		result += String.fromCharCode(randomIndex)
	}
	return result
}

function passwordSelection(correctPassword, alphabetFull, length) {
	const symbolsRegister = new Array(length).fill(0)

	while (true) {
		const currentPassword = formString(symbolsRegister, alphabetFull)

		if (currentPassword === correctPassword) {
			console.log('Пароль подобран: ' + currentPassword)
			break
		}
		increment(symbolsRegister, alphabetFull.length)
	}
}

function increment(symbolsRegister, alphabetLength) {
	for (let i = symbolsRegister.length - 1; i >= 0; i--) {
		symbolsRegister[i]++

		if (symbolsRegister[i] === alphabetLength) {
			symbolsRegister[i] = 0
		} else {
			break
		}
	}
}

function formString(symbolsRegister, alphabetFull) {
	let password = ''
	for (const index of symbolsRegister) {
		password += alphabetFull[index]
	}
	return password
}

function visualizeFrequencyDistribution(password) {
	const frequencyMap = new Map()

	for (let i = 0; i < password.length; i++) {
		const char = password.charAt(i)
		if (frequencyMap.has(char)) {
			frequencyMap.set(char, frequencyMap.get(char) + 1)
		} else {
			frequencyMap.set(char, 1)
		}
	}
	const sortedMap = new Map(
		[...frequencyMap].sort(([keyA], [keyB]) => {
			const asciiA = keyA.charCodeAt(0)
			const asciiB = keyB.charCodeAt(0)
			return asciiA - asciiB
		})
	)

	console.log('Частотное распределение символов:')
	for (const [char, frequency] of sortedMap) {
		const percentage = (frequency / password.length) * 100
		console.log(`${char}: ${percentage.toFixed(2)}%`)
	}
}

function main() {
	const passLength = 4
	console.log('Русские строчные и заглавные буквы\n')

	let alphabetFull = ALPHABET_RUS_UPPER + ALPHABET_RUS_LOWER

	const password = generatePassword(passLength)
	console.log(`Пароль длиной ${passLength} сгенерирован: ${password}`)

	console.log('______________Подбор пароля______________')
	console.log(
		'Количество возможных комбинаций ' +
			Math.pow(alphabetFull.length, passLength)
	)
	const start_time = new Date().getTime()
	passwordSelection(password, alphabetFull, passLength)
	const end_time = new Date().getTime()
	const time = (end_time - start_time) / 1000.0

	console.log('Time: ' + time + ' sec')
	console.log(
		'Количество возможных комбинаций ' +
			Math.pow(alphabetFull.length, passLength)
	)

	console.log('__________Распределение символов__________')
	const secondPass = generatePassword(1000000)
	visualizeFrequencyDistribution(secondPass)
}

main()
