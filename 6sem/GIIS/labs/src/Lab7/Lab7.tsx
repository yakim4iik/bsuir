import * as d3 from 'd3'
import React, { useEffect, useRef, useState } from 'react'
import './Lab7.css'

const Lab7: React.FC = () => {
	const svgRef = useRef<SVGSVGElement | null>(null)
	const [points, setPoints] = useState<[number, number][]>([])
	const [delaunay, setDelaunay] = useState<d3.Delaunay<
		[number, number]
	> | null>(null)
	const [voronoi, setVoronoi] = useState<d3.Voronoi<[number, number]> | null>(
		null
	)

	useEffect(() => {
		updateVisualization() // Инициальная отрисовка полигона
	}, [points])

	const updateVisualization = () => {
		const svg = d3.select(svgRef.current)

		// Очистка SVG-контейнера
		svg.selectAll('*').remove()

		// Визуализация триангуляции Делоне, если delaunay не равно null
		if (delaunay !== null) {
			svg
				.append('g')
				.attr('class', 'triangulation')
				.selectAll('path')
				.data(delaunay.trianglePolygons())
				.enter()
				.append('path')
				.attr('d', d => 'M' + d.join('L') + 'Z')
				.style('stroke', 'yellow')
				.style('stroke-width', 1)
				.style('fill', 'none')
		}

		// Визуализация точек
		svg
			.append('g')
			.attr('class', 'points')
			.selectAll('circle')
			.data(points)
			.enter()
			.append('circle')
			.attr('cx', d => d[0])
			.attr('cy', d => d[1])
			.attr('r', 3)

		// Визуализация диаграммы Вороного, если voronoi не равно null
		if (voronoi !== null) {
			svg
				.append('g')
				.attr('class', 'voronoi')
				.selectAll('path')
				.data(voronoi.cellPolygons())
				.enter()
				.append('path')
				.attr('d', d => 'M' + d.join('L') + 'Z')
				.style('stroke', 'black')
				.style('stroke-width', 1)
				.style('fill', 'none')
		}
	}

	const handleMouseClick = (event: React.MouseEvent<SVGSVGElement>) => {
		const point = d3.pointer(event, svgRef.current)

		setPoints(prevPoints => {
			const updatedPoints = [...prevPoints, point]
			const newDelaunay = d3.Delaunay.from(updatedPoints)
			const newVoronoi = newDelaunay.voronoi()

			setDelaunay(newDelaunay)
			setVoronoi(newVoronoi)
			updateVisualization()

			return updatedPoints
		})
	}

	const clearSvg = () => {
		const svg = svgRef.current
		if (svg) {
			svg.innerHTML = ''
			setPoints([])
			setDelaunay(null)
			setVoronoi(null)
		}
	}

	return (
		<div className='Lab7'>
			<div className='MainArea'>
				<svg
					ref={svgRef}
					id='visualization'
					className='Canvas7'
					style={{ width: '700px', height: '500px' }}
					onClick={handleMouseClick}
				/>
			</div>
			<div className='Menu7'>
				<button onClick={clearSvg}>Очистить</button>
			</div>
		</div>
	)
}

export default Lab7
