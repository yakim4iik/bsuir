import React, { useEffect, useRef, useState } from 'react'
import './Lab6.css'

function Lab6() {
	const [points, setPoints] = useState<{ x: number; y: number }[]>([])
	const [selectedAlgorithm, setSelectedAlgorithm] = useState<string>('')
	const [fillColor, setFillColor] = useState<string>('#000001')
	const canvasRef = useRef<HTMLCanvasElement | null>(null)
	const [selectedPoint, setSelectedPoint] = useState<{
		x: number
		y: number
	} | null>(null)
	const [isPolygonFilled, setIsPolygonFilled] = useState<boolean>(false)

	useEffect(() => {
		drawPolygon() // Initial polygon drawing
	}, [points])

	const handleAlgorithmChange = (selectedValue: string) => {
		setSelectedAlgorithm(selectedValue)
		switch (selectedValue) {
			case 'floodFill':
				if (selectedPoint !== null) {
					floodFill(selectedPoint.x, selectedPoint.y)
				}
				break
			case 'scanlineFill':
				if (selectedPoint !== null) {
					scanlineFillPolygon(selectedPoint.x, selectedPoint.y)
				}
				break
			default:
				break
		}
	}

	const handleColorChange = (event: React.ChangeEvent<HTMLInputElement>) => {
		setFillColor(event.target.value)
		setIsPolygonFilled(false)
		console.log(fillColor)
	}

	const clearCanvas = () => {
		const canvas = canvasRef.current
		if (canvas) {
			const context = canvas.getContext('2d')
			if (context) {
				context.clearRect(0, 0, canvas.width, canvas.height)
				context.beginPath()
				context.fillStyle = 'white'
			}
		}
		setPoints([])
		setIsPolygonFilled(false)
	}
	const addPoint = (event: React.MouseEvent<HTMLCanvasElement, MouseEvent>) => {
		const canvas = canvasRef.current
		if (canvas) {
			const rect = canvas.getBoundingClientRect()
			const x = event.clientX - rect.left
			const y = event.clientY - rect.top

			if (isPolygonFilled) {
				if (selectedAlgorithm === 'scanlineFill') {
					scanlineFillPolygon(x, y)
				} else if (selectedAlgorithm === 'floodFill') {
					floodFill(x, y)
				}
			} else {
				const newPoints = [...points, { x, y }]
				setPoints(newPoints)
				drawPoint(x, y)
				drawPolygon()
			}
		}
	}

	const drawPoint = (x: number, y: number) => {
		const canvas = canvasRef.current
		if (canvas) {
			const context = canvas.getContext('2d')
			if (context) {
				context.beginPath()
				context.arc(x, y, 3, 0, 2 * Math.PI)
				context.fillStyle = fillColor
				context.fill()
			}
		}
	}

	const drawLine = (
		x1: number,
		y1: number,
		x2: number,
		y2: number,
		color: string = fillColor
	) => {
		const canvas = canvasRef.current
		if (canvas) {
			const context = canvas.getContext('2d')
			if (context) {
				context.beginPath()
				context.moveTo(x1, y1)
				context.lineTo(x2, y2)
				context.strokeStyle = color
				context.stroke()
			}
		}
	}

	const drawPolygon = () => {
		const canvas = canvasRef.current
		if (canvas) {
			const context = canvas.getContext('2d')
			if (context) {
				context.clearRect(0, 0, canvas.width, canvas.height)
				for (let i = 0; i < points.length; i++) {
					const point = points[i]
					drawPoint(point.x, point.y)
					if (i > 0) {
						const prevPoint = points[i - 1]
						drawLine(prevPoint.x, prevPoint.y, point.x, point.y, fillColor)
					}
				}
				if (points.length > 2) {
					const lastPoint = points[points.length - 1]
					const firstPoint = points[0]
					drawLine(
						lastPoint.x,
						lastPoint.y,
						firstPoint.x,
						firstPoint.y,
						fillColor
					)
				}
			}
		}
	}

	const floodFill = (x: number, y: number): void => {
		x = Math.floor(x)
		y = Math.floor(y)
		const canvas = canvasRef.current
		if (canvas) {
			const context = canvas.getContext('2d')
			if (context) {
				const imageData = context.getImageData(
					0,
					0,
					canvas.width,
					canvas.height
				)
				const width = canvas.width
				const height = canvas.height
				const pixelStack: [number, number][] = []
				const baseColor = getPixelColor(x, y, imageData)
				const targetColor = hexToRgb(fillColor)

				if (!colorsMatch(baseColor, targetColor)) {
					pixelStack.push([x, y])

					const intervalId = setInterval(() => {
						if (pixelStack.length === 0) {
							clearInterval(intervalId)
							context.putImageData(imageData, 0, 0)
							setIsPolygonFilled(true)
							return
						}

						const newPos = pixelStack.pop()
						if (newPos) {
							let [newX, newY] = newPos

							let currentPos = newY * width + newX

							while (
								newY >= 0 &&
								colorsMatch(baseColor, getPixelColor(newX, newY, imageData))
							) {
								currentPos -= width
								newY--
							}

							newY++
							currentPos += width

							let reachLeft = false
							let reachRight = false

							while (
								newY < height &&
								colorsMatch(baseColor, getPixelColor(newX, newY, imageData))
							) {
								setPixelColor(newX, newY, targetColor, imageData)

								if (
									newX > 0 &&
									colorsMatch(
										baseColor,
										getPixelColor(newX - 1, newY, imageData)
									)
								) {
									if (!reachLeft) {
										pixelStack.push([newX - 1, newY])
										reachLeft = true
									}
								} else if (reachLeft) {
									reachLeft = false
								}

								if (
									newX < width - 1 &&
									colorsMatch(
										baseColor,
										getPixelColor(newX + 1, newY, imageData)
									)
								) {
									if (!reachRight) {
										pixelStack.push([newX + 1, newY])
										reachRight = true
									}
								} else if (reachRight) {
									reachRight = false
								}

								newY++
								currentPos += width
							}

							context.putImageData(imageData, 0, 0)
						}
					}, 10)
				}
			}
		}
	}

	function hexToRgb(hex: string): [number, number, number] {
		const parsedHex = hex.replace(/^#/, '')
		const r = parseInt(parsedHex.substring(0, 2), 16)
		const g = parseInt(parsedHex.substring(2, 4), 16)
		const b = parseInt(parsedHex.substring(4, 6), 16)
		return [r, g, b]
	}

	const colorsMatch = (color1: number[], color2: number[]): boolean => {
		return (
			color1[0] === color2[0] &&
			color1[1] === color2[1] &&
			color1[2] === color2[2]
		)
	}

	const getPixelColor = (
		x: number,
		y: number,
		imageData: ImageData
	): number[] => {
		const pixelIndex = (y * imageData.width + x) * 4
		return [
			imageData.data[pixelIndex],
			imageData.data[pixelIndex + 1],
			imageData.data[pixelIndex + 2],
		]
	}

	const setPixelColor = (
		x: number,
		y: number,
		color: number[],
		imageData: ImageData
	): void => {
		const pixelIndex = (y * imageData.width + x) * 4
		imageData.data[pixelIndex] = color[0]
		imageData.data[pixelIndex + 1] = color[1]
		imageData.data[pixelIndex + 2] = color[2]
		imageData.data[pixelIndex + 3] = 255
	}

	const scanlineFillPolygon = (x: number, y: number): void => {
		// Алгоритм растровой развертки с упорядоченным списком ребер
		const edgeList: {
			yMin: number
			yMax: number
			xMin: number
			inverseSlope: number
		}[] = []

		for (let i = 0; i < points.length; i++) {
			const currentPoint = points[i]
			const nextPoint = points[(i + 1) % points.length]

			if (currentPoint.y !== nextPoint.y) {
				const edge: {
					yMin: number
					yMax: number
					xMin: number
					inverseSlope: number
				} = {
					yMin: Math.min(currentPoint.y, nextPoint.y),
					yMax: Math.max(currentPoint.y, nextPoint.y),
					xMin: currentPoint.y < nextPoint.y ? currentPoint.x : nextPoint.x,
					inverseSlope:
						(nextPoint.x - currentPoint.x) / (nextPoint.y - currentPoint.y),
				}

				edgeList.push(edge)
			}
		}

		edgeList.sort((a, b) => a.yMin - b.yMin)

		const activeEdgeList: {
			yMax: number
			xMin: number
			inverseSlope: number
		}[] = []

		for (
			let scanlineY = edgeList[0].yMin;
			scanlineY <= edgeList[edgeList.length - 1].yMax;
			scanlineY++
		) {
			for (let i = 0; i < edgeList.length; i++) {
				const edge = edgeList[i]

				if (edge.yMin === scanlineY) {
					activeEdgeList.push({
						yMax: edge.yMax,
						xMin: edge.xMin,
						inverseSlope: edge.inverseSlope,
					})
				} else if (edge.yMax === scanlineY) {
					activeEdgeList.splice(
						activeEdgeList.findIndex(
							activeEdge => activeEdge.yMax === edge.yMax
						),
						1
					)
				}
			}

			activeEdgeList.sort((a, b) => a.xMin - b.xMin)
			for (let i = 0; i < activeEdgeList.length; i += 2) {
				const startEdge = activeEdgeList[i]
				const endEdge = activeEdgeList[i + 1]

				for (let x = Math.ceil(startEdge.xMin); x < endEdge.xMin; x++) {
					setTimeout(() => drawPoint(x, scanlineY), 1)
				}
			}

			for (let i = 0; i < activeEdgeList.length; i++) {
				activeEdgeList[i].xMin += activeEdgeList[i].inverseSlope
			}
		}
	}

	const savePolygon = () => {
		const polygon = {
			points: [...points],
			fillColor: fillColor,
		}
		setIsPolygonFilled(true)
	}

	return (
		<div className='Lab6'>
			<div className='MainArea'>
				<canvas
					id='svg'
					ref={canvasRef}
					className='Canvas6'
					width={700}
					height={500}
					onClick={addPoint}
				></canvas>
			</div>
			<div className='Menu6'>
				<label htmlFor='color'>Цвет заливки:</label>
				<input
					type='color'
					id='color'
					value={fillColor}
					onChange={handleColorChange}
				/>
				<div className='algorithm-container'>
					<label htmlFor='algorithm'>Алгоритм заливки:</label>
					<button
						className={selectedAlgorithm === 'floodFill' ? 'active' : ''}
						onClick={() => handleAlgorithmChange('floodFill')}
					>
						Затравка
					</button>
					<button
						className={selectedAlgorithm === 'scanlineFill' ? 'active' : ''}
						onClick={() => handleAlgorithmChange('scanlineFill')}
					>
						Развертка
					</button>
				</div>
				<button onClick={savePolygon}>Сохранить полигон</button>
				<button onClick={clearCanvas}>Очистить</button>
			</div>
		</div>
	)
}

export default Lab6
