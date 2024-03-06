import React, { useState } from 'react'
import {
	bresenhamAlgorithm,
	digitalDifferentialAnalyzer,
	xiaolinWuAlgorithm,
} from '../algoritmFirst'
import Point, { Color } from '../drawingData'

import './Lab1.css'

const Lab1: React.FC = () => {
	const [segmentEnds, setSegmentEnds] = useState<Point[]>([])
	const [points, setPoints] = useState<Point[]>([])
	const [color, setColor] = useState<Color>({ r: 196, g: 223, b: 230 })

	const [selectedAlgorithm, setSelectedAlgorithm] = useState<string>(
		'digitalDifferentialAnalyzer'
	)
	const [showGrid, setShowGrid] = useState<boolean>(false)
	const [debug, setDebug] = useState<boolean>(false)
	const [debugRunning, setDebugRunning] = useState<boolean>(false)
	const [counter, setCounter] = useState<number>(0)

	const width = 700
	const height = 500
	const cellSize = 15

	const handleAlgorithmChange = (
		event: React.ChangeEvent<HTMLSelectElement>
	) => {
		const selectedValue = event.target.value
		setSelectedAlgorithm(selectedValue)
	}

	const handleRun = () => {
		setCounter(0)
		setDebugRunning(debug)

		let newPoints: Point[] = []

		switch (selectedAlgorithm) {
			case 'digitalDifferentialAnalyzer':
				newPoints = digitalDifferentialAnalyzer(segmentEnds, color)
				break
			case 'bresenhamAlgorithm':
				newPoints = bresenhamAlgorithm(segmentEnds, color)
				break
			case 'xiaolinWuAlgorithm':
				newPoints = xiaolinWuAlgorithm(segmentEnds, color)
				break
			default:
				alert("You didn't choose an algorithm")
				break
		}

		setPoints(newPoints)
	}

	const handleStep = () => {
		if (counter === points.length) {
			setDebugRunning(false)
			return
		}
		setCounter(prevCounter => prevCounter + 1)
	}

	const handleReset = () => {
		setCounter(0)
		setPoints([])
		setSegmentEnds([])
		setDebugRunning(false)
	}

	const toggleDebug = () => {
		setDebug(!debug)
		setShowGrid(!showGrid)
	}

	const createSegment = (
		event: React.MouseEvent<SVGSVGElement, MouseEvent>
	): void => {
		const svg = event.currentTarget
		const pt = svg.createSVGPoint()
		pt.x = event.clientX
		pt.y = event.clientY
		const screenCTM = svg.getScreenCTM()

		if (screenCTM && screenCTM.inverse) {
			const inverseCTM = screenCTM.inverse()

			if (inverseCTM) {
				const cursorPt = pt.matrixTransform(inverseCTM)

				const point: Point = {
					x: Math.floor(cursorPt.x / cellSize),
					y: Math.floor(cursorPt.y / cellSize),
					opacity: 1,
					color: { r: 196, g: 223, b: 230 },
				}

				if (segmentEnds.length === 2) {
					handleReset()
					setSegmentEnds([point])
				} else {
					setSegmentEnds(prevSegmentEnds => [...prevSegmentEnds, point])
				}
			}
		}
	}

	return (
		<div className='Wrapper'>
			<div className='MainArea'>
				<svg
					className='Svg'
					onClick={createSegment}
					xmlns='http://www.w3.org/2000/svg'
					width={width}
					height={height}
				>
					{showGrid &&
						Array.from({ length: Math.ceil(width / cellSize) }).map(
							(_, indexX) =>
								Array.from({ length: Math.ceil(height / cellSize) }).map(
									(_, indexY) => (
										<rect
											className='GridCell'
											key={`${indexX}-${indexY}`}
											x={indexX * cellSize}
											y={indexY * cellSize}
											width={cellSize}
											height={cellSize}
										/>
									)
								)
						)}
					{segmentEnds.map((point, index) => (
						<rect
							key={index}
							x={point.x * cellSize}
							y={point.y * cellSize}
							width={cellSize}
							height={cellSize}
							fill={`rgba(${point.color.r}, ${point.color.g}, ${point.color.b}, ${point.opacity})`}
						/>
					))}
					{(debug ? points.slice(0, counter) : points).map((point, index) => (
						<rect
							key={index}
							x={point.x * cellSize}
							y={point.y * cellSize}
							width={cellSize}
							height={cellSize}
							fill={`rgba(${point.color.r}, ${point.color.g}, ${point.color.b}, ${point.opacity})`}
						/>
					))}
				</svg>
				<div className='Menu1'>
					<div className='Input'>
						<label>Алгоритм </label>
						<div className='AlgorithmButtons'>
							<button
								className={`AlgorithmButton ${
									selectedAlgorithm === 'digitalDifferentialAnalyzer'
										? 'active'
										: ''
								}`}
								onClick={() =>
									setSelectedAlgorithm('digitalDifferentialAnalyzer')
								}
							>
								Алгоритм ЦДА
							</button>
							<button
								className={`AlgorithmButton ${
									selectedAlgorithm === 'bresenhamAlgorithm' ? 'active' : ''
								}`}
								onClick={() => setSelectedAlgorithm('bresenhamAlgorithm')}
							>
								Алгоритм Брезенхема
							</button>
							<button
								className={`AlgorithmButton ${
									selectedAlgorithm === 'xiaolinWuAlgorithm' ? 'active' : ''
								}`}
								onClick={() => setSelectedAlgorithm('xiaolinWuAlgorithm')}
							>
								Алгоритм Ву
							</button>
						</div>
					</div>
					<div className='debugSettings'>
						<div>
							<label>Отладка: </label>
							<input type='checkbox' checked={debug} onChange={toggleDebug} />
						</div>
					</div>
					<div className='Buttons'>
						{!debugRunning && (
							<button className='Run' onClick={handleRun}>
								Старт
							</button>
						)}
						{debugRunning && (
							<button className='Step' onClick={handleStep}>
								Дальше
							</button>
						)}
					</div>
				</div>
			</div>
		</div>
	)
}

export default Lab1
