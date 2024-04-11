import * as d3 from 'd3'
import React, { useEffect, useRef, useState } from 'react'
import Point from '../drawingData'
import './Lab3.css'

function Lab3() {
	const [segmentEnds, setSegmentEnds] = useState<Point[]>([])
	const svgRef = useRef<SVGSVGElement | null>(null)
	const [selectedAlgorithm, setSelectedAlgorithm] = useState<string>('hermite')
	const [color, setColor] = useState<string>('rgba(255, 255, 255)')
	const [cellSize, setCellSize] = useState<number>(1)

	useEffect(() => {
		const storedAlgorithm = localStorage.getItem('selectedAlgorithm')
		if (storedAlgorithm) {
			setSelectedAlgorithm(storedAlgorithm)
		}
	}, [])

	const handleAlgorithmChange = (selectedValue: string) => {
		setSelectedAlgorithm(selectedValue)
		localStorage.setItem('selectedAlgorithm', selectedValue)
	}

	const clearSvg = () => {
		const svg = svgRef.current
		if (svg) {
			svg.innerHTML = ''
		}
	}

	const handleMouseDown = (
		event: React.MouseEvent<SVGSVGElement, MouseEvent>
	): void => {
		const svg = event.currentTarget
		const pt = svg.createSVGPoint()
		pt.x = event.clientX - svg.getBoundingClientRect().left
		pt.y = event.clientY - svg.getBoundingClientRect().top

		const point: Point = {
			x: Math.floor(pt.x / cellSize),
			y: Math.floor(pt.y / cellSize),
			color: { r: 102, g: 0, b: 51 },
			opacity: 0,
		}
		setSegmentEnds(prevSegmentEnds => [...prevSegmentEnds, point])
		if (segmentEnds.length >= 2) drawCurve()
	}

	const hermiteAlgorithm = () => {
		const svg = svgRef.current
		console.log('hermite')
		clearSvg()
		if (svg) {
			for (let i = 0; i < segmentEnds.length - 1; i++) {
				const p0 = segmentEnds[i]
				const p1 = segmentEnds[i + 1]
				const t0 = i > 0 ? (p1.x - segmentEnds[i - 1].x) / 2 : 0
				const t1 =
					i < segmentEnds.length - 2 ? (segmentEnds[i + 2].x - p0.x) / 2 : 0

				let d = ''
				for (let t = 0; t <= 1; t += 0.01) {
					const h1 = 2 * Math.pow(t, 3) - 3 * Math.pow(t, 2) + 1
					const h2 = -2 * Math.pow(t, 3) + 3 * Math.pow(t, 2)
					const h3 = Math.pow(t, 3) - 2 * Math.pow(t, 2) + t
					const h4 = Math.pow(t, 3) - Math.pow(t, 2) //базисных функций Ермита.

					const x = h1 * p0.x + h2 * p1.x + h3 * t0 + h4 * t1
					const y = h1 * p0.y + h2 * p1.y + h3 * t0 + h4 * t1

					if (t === 0) {
						d += `M ${x} ${y}`
					} else {
						d += ` L ${x} ${y}`
					}
				}

				const path = document.createElementNS(
					'http://www.w3.org/2000/svg',
					'path'
				)
				path.setAttribute('d', d)
				path.setAttribute('stroke', 'rgb(0, 23, 21)')
				path.setAttribute('fill', 'none')
				path.setAttribute('stroke-width', '2')
				svg.appendChild(path)
			}
		}
	}

	const bezierAlgorithm = () => {
		const svg = svgRef.current
		console.log('bezier')
		if (svg) {
			if (segmentEnds.length >= 4 && (segmentEnds.length - 1) % 3 === 0) {
				clearSvg()
				for (let i = 0; i < segmentEnds.length - 1; i += 3) {
					const p0 = segmentEnds[i]
					const p1 = segmentEnds[i + 1]
					const p2 = segmentEnds[i + 2]
					const p3 = segmentEnds[i + 3]

					const iterations = 10000
					let d = ''
					for (let j = 0; j <= iterations; j++) {
						const t = j / iterations

						const x =
							Math.pow(1 - t, 3) * p0.x +
							3 * Math.pow(1 - t, 2) * t * p1.x +
							3 * (1 - t) * Math.pow(t, 2) * p2.x +
							Math.pow(t, 3) * p3.x //кубическую интерполяцию для вычисления координат x и y новой точки на кривой Безье.
						const y =
							Math.pow(1 - t, 3) * p0.y +
							3 * Math.pow(1 - t, 2) * t * p1.y +
							3 * (1 - t) * Math.pow(t, 2) * p2.y +
							Math.pow(t, 3) * p3.y

						if (j === 0) {
							d += `M ${x} ${y}`
						} else {
							d += ` L ${x} ${y}`
						}
					}

					const path = document.createElementNS(
						'http://www.w3.org/2000/svg',
						'path'
					)
					path.setAttribute('d', d)
					path.setAttribute('stroke', 'rgb(0, 23, 21)')
					path.setAttribute('fill', 'none')
					path.setAttribute('stroke-width', '2')
					svg.appendChild(path)
				}
			}
		}
	}

	const bSplineAlgorithm = () => {
		const svg = svgRef.current
		console.log('b-spline')
		if (svg) {
			if (segmentEnds.length >= 4) {
				clearSvg()

				// Convert the segmentEnds data to the format expected by d3.js
				const points = segmentEnds.map(point => ({ x: point.x, y: point.y }))

				// Set up scales for x and y coordinates
				const xScale = d3
					.scaleLinear()
					.domain([0, d3.max(points, d => d.x) as number])
					.range([0, d3.max(points, d => d.x) || 0])

				const yScale = d3
					.scaleLinear()
					.domain([0, d3.max(points, d => d.y) as number])
					.range([0, d3.max(points, d => d.y) || 0])

				// Create the B-spline generator
				const lineGenerator = d3
					.line<{ x: number; y: number }>() // Specify the type for the 'd' parameter
					.x(d => xScale(d.x))
					.y(d => yScale(d.y))
					.curve(d3.curveNatural)

				// Generate the B-spline path
				const pathData = lineGenerator(points)

				if (pathData) {
					// Add null check
					// Create an SVG path element for the B-spline curve
					const path = document.createElementNS(
						'http://www.w3.org/2000/svg',
						'path'
					)
					path.setAttribute('d', pathData)
					path.setAttribute('stroke', 'rgb(0, 23, 21)')
					path.setAttribute('fill', 'none')
					path.setAttribute('stroke-width', '2')

					// Append the SVG path element to the SVG container
					svg.appendChild(path)
				}
			}
		}
	}

	const drawCurve = () => {
		switch (selectedAlgorithm) {
			case 'hermite':
				hermiteAlgorithm()
				break
			case 'bezier':
				bezierAlgorithm()
				break
			case 'spline':
				bSplineAlgorithm()
				break
			default:
				alert("You didn't choose algorithm")
				break
		}
	}

	const clear = () => {
		const svg = svgRef.current
		if (svg) {
			svg.innerHTML = ''
		}
		window.location.reload()
	}

	return (
		<div className='Lab3'>
			<div className='MainArea'>
				<svg id='svg' ref={svgRef} className='Svg3' onClick={handleMouseDown}>
					{segmentEnds.map((point, index) => (
						<circle
							key={index}
							cx={point.x * cellSize}
							cy={point.y * cellSize}
							r={3}
							fill={color}
						/>
					))}
				</svg>
			</div>
			<div className='Menu3'>
				<div className='algorithm-container'>
					<p className='algorithm-label'>Алгоритм</p>
					<button
						className={selectedAlgorithm === 'hermite' ? 'active' : ''}
						onClick={() => handleAlgorithmChange('hermite')}
					>
						Интерполяция Эрмита
					</button>
					<button
						className={selectedAlgorithm === 'bezier' ? 'active' : ''}
						onClick={() => handleAlgorithmChange('bezier')}
					>
						Формы Безье
					</button>
					<button
						className={selectedAlgorithm === 'spline' ? 'active' : ''}
						onClick={() => handleAlgorithmChange('spline')}
					>
						B-сплайн
					</button>
				</div>
				<button className='clearSvg' onClick={clear}>
					Очистить
				</button>
			</div>
		</div>
	)
}

export default Lab3
