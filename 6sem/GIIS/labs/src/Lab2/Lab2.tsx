import React, { useRef, useState } from 'react'
import './Lab2.css'

function Lab2() {
	const canvasRef = useRef<SVGSVGElement | null>(null)
	const [centerX, setCenterX] = useState<number | null>(null)
	const [centerY, setCenterY] = useState<number | null>(null)
	const [isDrawing, setIsDrawing] = useState(false)
	const [curveType, setCurveType] = useState('circle')

	const startDrawing = (event: React.MouseEvent<SVGSVGElement>) => {
		setIsDrawing(true)
		const canvas = canvasRef.current
		if (canvas) {
			const rect = canvas.getBoundingClientRect()
			setCenterX(event.clientX - rect.left)
			setCenterY(event.clientY - rect.top)
		}
	}

	const drawCircle = (centerX: number, centerY: number, radius: number) => {
		const step = (1 / radius) * 3
		let x: number, y: number

		for (let angle = 0; angle < 2 * Math.PI; angle += step) {
			x = centerX + radius * Math.cos(angle)
			y = centerY + radius * Math.sin(angle)

			drawPoint(x, y)
		}
	}

	const drawEllipse = (
		centerX: number,
		centerY: number,
		radiusX: number,
		radiusY: number
	) => {
		const step = (1 / Math.max(radiusX, radiusY)) * 3
		let x: number, y: number

		for (let angle = 0; angle < 2 * Math.PI; angle += step) {
			x = centerX + radiusX * Math.cos(angle)
			y = centerY + radiusY * Math.sin(angle)

			drawPoint(x, y)
		}
	}

	const drawHyperbola = (
		centerX: number,
		centerY: number,
		a: number,
		b: number
	) => {
		const step = 1 / b
		let x: number, y: number

		for (let angle = 0; angle < 2 * Math.PI; angle += step) {
			x = centerX + a / Math.cos(angle)
			y = centerY + b * Math.tan(angle)

			drawPoint(x, y)
		}
	}

	const drawParabola = (
		centerX: number,
		centerY: number,
		a: number,
		b: number
	) => {
		const step = 1 / b
		let x: number, y: number

		for (let xVal = -50; xVal <= 50; xVal += step) {
			x = centerX + a * xVal
			y = centerY + b * Math.pow(xVal, 2)

			drawPoint(x, y)

			// Рисование нижней ветки параболы
			// drawPoint(x, 2 * centerY - y)
		}
	}

	const drawPoint = (x: number, y: number) => {
		const canvas = canvasRef.current
		if (canvas) {
			const rect = document.createElementNS(
				'http://www.w3.org/2000/svg',
				'rect'
			)
			rect.setAttribute('x', String(x))
			rect.setAttribute('y', String(y))
			rect.setAttribute('width', '1')
			rect.setAttribute('height', '1')
			rect.setAttribute('fill', 'black')
			canvas.appendChild(rect)
		}
	}

	const draw = (event: React.MouseEvent<SVGSVGElement>) => {
		if (!isDrawing) return
		const canvas = canvasRef.current
		if (canvas) {
			const rect = canvas.getBoundingClientRect()
			const a = Math.abs(event.clientX - rect.left - (centerX || 0))
			const b = Math.abs(event.clientY - rect.top - (centerY || 0))

			canvas.innerHTML = ''

			switch (curveType) {
				case 'circle':
					drawCircle(centerX || 0, centerY || 0, a)
					break
				case 'ellipse':
					drawEllipse(centerX || 0, centerY || 0, a, b)
					break
				case 'hyperbola':
					drawHyperbola(centerX || 0, centerY || 0, a, b)
					break
				case 'parabola':
					drawParabola(centerX || 0, centerY || 0, a, b)
					break
				default:
					break
			}
		}
	}

	const stopDrawing = () => {
		setIsDrawing(false)
	}

	return (
		<div className='Lab2'>
			<div className='MainArea'>
				<svg
					id='canvas'
					ref={canvasRef}
					onMouseDown={startDrawing}
					onMouseMove={draw}
					onMouseUp={stopDrawing}
					className='Svg2'
				></svg>
			</div>
			<div className='Menu2'>
				<p className='algorithm-label'>Алгоритм</p>
				<div className='algoritm-button'>
					<button
						className={curveType === 'circle' ? 'active' : ''}
						onClick={() => setCurveType('circle')}
					>
						Круг
					</button>
					<button
						className={curveType === 'ellipse' ? 'active' : ''}
						onClick={() => setCurveType('ellipse')}
					>
						Эллипс
					</button>
					<button
						className={curveType === 'hyperbola' ? 'active' : ''}
						onClick={() => setCurveType('hyperbola')}
					>
						Гипербола
					</button>
					<button
						className={curveType === 'parabola' ? 'active' : ''}
						onClick={() => setCurveType('parabola')}
					>
						Парабола
					</button>
				</div>
			</div>
		</div>
	)
}

export default Lab2
