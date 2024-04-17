import React, { useEffect, useRef, useState } from 'react'
import './Lab5.css'

function Lab5() {
	const [points, setPoints] = useState<{ x: number; y: number }[]>([])
	const [selectedAlgorithm, setSelectedAlgorithm] =
		useState<string>('convexity')
	const canvasRef = useRef<HTMLCanvasElement | null>(null)

	useEffect(() => {
		drawPolygon() // Инициальная отрисовка полигона
	}, [points])

	const handleAlgorithmChange = (selectedValue: string) => {
		switch (selectedValue) {
			case 'convexity':
				checkConvexity()
				break
			case 'graham':
				computeConvexHullGraham()
				break
			case 'jarvis':
				computeConvexHullJarvis()
				break
			default:
				break
		}
	}

	const clearCanvas = () => {
		const canvas = canvasRef.current
		if (canvas) {
			const context = canvas.getContext('2d')
			if (context) {
				context.clearRect(0, 0, canvas.width, canvas.height)
			}
		}
		setPoints([]) // Очистка массива points
	}

	const addPoint = (event: React.MouseEvent<HTMLCanvasElement, MouseEvent>) => {
		const canvas = canvasRef.current
		if (canvas) {
			const rect = canvas.getBoundingClientRect()
			const x = event.clientX - rect.left
			const y = event.clientY - rect.top
			const newPoints = [...points, { x, y }]
			setPoints(newPoints)
			drawPoint(x, y)
			drawPolygon()
			setPoints(newPoints)
		}
	}

	const checkConvexity = () => {
		if (points.length < 3) {
			alert('Создай полигон')
			return
		}
		const orientation = getOrientation(points[0], points[1], points[2])
		const isClockwise = orientation < 0

		for (let i = 1; i < points.length; i++) {
			const p1 = points[i]
			const p2 = points[(i + 1) % points.length]
			const p3 = points[(i + 2) % points.length]

			const currentOrientation = getOrientation(p1, p2, p3)
			if (
				(currentOrientation < 0 && !isClockwise) ||
				(currentOrientation > 0 && isClockwise)
			) {
				alert('Полигон невыпуклый')
				return
			}
		}

		alert('Полигон выпуклый')
	}

	const getOrientation = (
		p1: { x: number; y: number },
		p2: { x: number; y: number },
		p3: { x: number; y: number }
	) => {
		const val = (p2.y - p1.y) * (p3.x - p2.x) - (p2.x - p1.x) * (p3.y - p2.y)
		if (val === 0) {
			return 0
		} else if (val > 0) {
			return 1
		} else {
			return -1
		}
	}

	const drawPoint = (x: number, y: number) => {
		const canvas = canvasRef.current
		if (canvas) {
			const context = canvas.getContext('2d')
			if (context) {
				context.beginPath()
				context.arc(x, y, 3, 0, 2 * Math.PI)
				context.fillStyle = 'black'
				context.fill()
			}
		}
	}

	const drawLine = (
		x1: number,
		y1: number,
		x2: number,
		y2: number,
		color: string = 'black'
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
				console.log(points.length)
				for (let i = 0; i < points.length; i++) {
					const point = points[i]
					drawPoint(point.x, point.y)
					if (i > 0) {
						const prevPoint = points[i - 1]
						drawLine(prevPoint.x, prevPoint.y, point.x, point.y, 'blue')
					}
				}
				if (points.length > 2) {
					const lastPoint = points[points.length - 1]
					const firstPoint = points[0]
					drawLine(lastPoint.x, lastPoint.y, firstPoint.x, firstPoint.y, 'blue')
				}
			}
		}
	}

	function calculateNormals() {
		if (points.length < 3) {
			alert('Создай полигон')
			return
		}

		const canvas = canvasRef.current
		drawPolygon()

		for (let i = 0; i < points.length; i++) {
			const currPoint = points[i]
			const nextPoint = points[(i + 1) % points.length]

			const normalX: number = nextPoint.y - currPoint.y
			const normalY: number = currPoint.x - nextPoint.x

			const normalLength: number = Math.sqrt(
				normalX * normalX + normalY * normalY
			)
			const normalizedNormalX: number = normalX / normalLength
			const normalizedNormalY: number = normalY / normalLength

			const normalStartX: number = currPoint.x + normalizedNormalX * 100
			const normalStartY: number = currPoint.y + normalizedNormalY * 100

			const normalEndX: number = currPoint.x - normalizedNormalX * 100
			const normalEndY: number = currPoint.y - normalizedNormalY * 100

			drawLine(normalStartX, normalStartY, normalEndX, normalEndY, 'red')
		}
	}

	const computeConvexHullGraham = () => {
		if (points.length < 3) {
			alert('Создай полигон')
			return
		}

		const sortedPoints = [...points].sort((a, b) => {
			if (a.y === b.y) {
				return a.x - b.x
			}
			return a.y - b.y
		})

		const hullPoints: { x: number; y: number }[] = []
		hullPoints.push(sortedPoints[0])
		hullPoints.push(sortedPoints[1])

		for (let i = 2; i < sortedPoints.length; i++) {
			while (
				hullPoints.length >= 2 &&
				getOrientation(
					hullPoints[hullPoints.length - 2],
					hullPoints[hullPoints.length - 1],
					sortedPoints[i]
				) <= 0
			) {
				hullPoints.pop()
			}
			hullPoints.push(sortedPoints[i])
		}

		setPoints(hullPoints)
	}

	const computeConvexHullJarvis = () => {
		if (points.length < 3) {
			alert('Создай полигон')
			return
		}

		const leftmostPoint = points.reduce((a, b) => (a.x < b.x ? a : b))
		let currentPoint = leftmostPoint
		const hullPoints: { x: number; y: number }[] = []

		let nextPoint: { x: number; y: number }
		do {
			hullPoints.push(currentPoint)
			nextPoint = points[0]

			for (let i = 1; i < points.length; i++) {
				if (
					nextPoint === currentPoint ||
					getOrientation(currentPoint, nextPoint, points[i]) < 0
				) {
					nextPoint = points[i]
				}
			}

			currentPoint = nextPoint
		} while (currentPoint !== leftmostPoint)

		setPoints(hullPoints)
	}

	return (
		<div className='Lab5'>
			<div className='MainArea'>
				<canvas
					id='svg'
					className='Svg5'
					ref={canvasRef}
					width={700}
					height={500}
					onClick={addPoint}
				></canvas>
			</div>
			<div className='Menu5'>
				<div className='algorithm-container'>
					<p className='algorithm-label'>Алгоритм:</p>
					<button
						className={selectedAlgorithm === 'convexity' ? 'active' : ''}
						onClick={() => handleAlgorithmChange('convexity')}
					>
						Проверка выпуклости
					</button>
					<button
						className={selectedAlgorithm === 'graham' ? 'active' : ''}
						onClick={() => handleAlgorithmChange('graham')}
					>
						Метод обхода Грэхема
					</button>
					<button
						className={selectedAlgorithm === 'jarvis' ? 'active' : ''}
						onClick={() => handleAlgorithmChange('jarvis')}
					>
						Метод Джарвиса
					</button>
				</div>
				<button onClick={calculateNormals}>Normalize</button>
				<button onClick={clearCanvas}>Clear</button>
			</div>
		</div>
	)
}

export default Lab5
