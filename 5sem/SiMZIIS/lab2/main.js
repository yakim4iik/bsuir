function encrypt(text, rows, columns) {
	text = text.replace(/\s/g, '')
	let encryptedText = ''

	const table = []
	for (let i = 0; i < rows; i++) {
		const row = []
		for (let j = i * columns; j < i * columns + columns; j++) {
			row.push(text[j])
		}
		table.push(row)
	}

	for (let i = 0; i < columns; i++) {
		for (let j = 0; j < rows; j++) {
			encryptedText += table[j][i]
		}
	}

	return {
		encryptedText,
		table,
	}
}

function decrypt(encryptedText, rows, columns) {
	let decryptedText = ''

	const table = []
	for (let i = 0; i < rows; i++) {
		const row = []
		for (let j = i; j < encryptedText.length; j += rows) {
			row.push(encryptedText[j])
		}
		table.push(row)
	}

	for (let i = 0; i < rows; i++) {
		for (let j = 0; j < columns; j++) {
			decryptedText += table[i][j]
		}
	}

	return {
		decryptedText: decryptedText.trim(),
		table,
	}
}

function bruteForceAttack(ciphertext, plaintext) {
	const maxRows = Math.ceil(ciphertext.length / 2)
	const maxColumns = Math.ceil(ciphertext.length / 2)

	let bestDecryption = ''
	let bestKey = ''
	for (let rows = 1; rows <= maxRows; rows++) {
		for (let columns = 1; columns <= maxColumns; columns++) {
			const { decryptedText } = decrypt(ciphertext, rows, columns)

			if (decryptedText.toLowerCase() === plaintext.toLowerCase()) {
				bestDecryption = decryptedText
				bestKey = `${rows}x${columns}`
				break
			}
		}
	}

	return {
		bestDecryption,
		bestKey,
	}
}

const plaintext = 'ЭТО ШИФР ДРЕВНЕЙ СПАРТЫ'
const rows = 4
const columns = 5

const { encryptedText, table: encryptedTable } = encrypt(
	plaintext,
	rows,
	columns
)
const { decryptedText, table: decryptedTable } = decrypt(
	encryptedText,
	rows,
	columns
)
console.log('Таблица для шифрования:', encryptedTable)
console.log('Зашифрованный текст:', encryptedText)

console.log('Таблица для расшифрования:', decryptedTable)
console.log('Расшифрованный текст:', decryptedText)

const startTime = new Date().getTime()
const attackResult = bruteForceAttack(
	'ПЕАООРТНКВИИПОИВВРПЧ',
	'ПРИВЕТИВАНПРОКОПОВИЧ'
)
const endTime = new Date().getTime()
const time = endTime - startTime
console.log(
	'Расшифрование подбором: ',
	attackResult.bestDecryption,
	'|| За время: ',
	time,
	'мс'
)
console.log('Ключ:', attackResult.bestKey)
