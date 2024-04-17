import Point, { Color } from './drawingData'

export const digitalDifferentialAnalyzer = (
	points: Point[],
	color: Color
): Point[] => {
	if (points.length != 2) return []

	const start = points[0]
	const end = points[1]

	const length = Math.max(Math.abs(start.x - end.x), Math.abs(start.y - end.y))

	const deltaX = -(start.x - end.x) / length
	const deltaY = -(start.y - end.y) / length

	const newPoints = []
	for (let i = 0; i < length + 1; i++) {
		const currentPoint: Point = {
			x: Math.round(start.x + i * deltaX),
			y: Math.round(start.y + i * deltaY),
			opacity: 1,
			color: color,
		}
		newPoints.push(currentPoint)
	}
	return newPoints
}

export const bresenhamAlgorithm = (points: Point[], color: Color): Point[] => {
	if (points.length !== 2) return []

	const start = points[0]
	const end = points[1]

	let currentX = start.x
	let currentY = start.y

	const deltaX = Math.abs(end.x - start.x)
	const deltaY = Math.abs(end.y - start.y)

	const stepX = start.x < end.x ? 1 : -1
	const stepY = start.y < end.y ? 1 : -1

	let error = deltaX - deltaY
	const newPoints: Point[] = []
	while (currentX !== end.x || currentY !== end.y) {
		newPoints.push({ x: currentX, y: currentY, opacity: 1, color: color })
		const doubleError = error * 2
		if (doubleError > -deltaY) {
			error -= deltaY
			currentX += stepX
		}
		if (doubleError < deltaX) {
			error += deltaX
			currentY += stepY
		}
	}
	newPoints.push({ x: currentX, y: currentY, opacity: 1, color: color })
	return newPoints
}

export const xiaolinWuAlgorithm = (points: Point[], color: Color): Point[] => {
	if (points.length !== 2) return []

	let start = { ...points[0] }
	let end = { ...points[1] }

	const steep = Math.abs(end.y - start.y) > Math.abs(end.x - start.x)

	if (steep) {
		;[start.x, start.y] = [start.y, start.x]
		;[end.x, end.y] = [end.y, end.x]
	}
	if (start.x > end.x) {
		;[start, end] = [end, start]
	}

	const deltaX = end.x - start.x
	const deltaY = end.y - start.y
	const gradient = deltaX === 0 ? 0 : deltaY / deltaX

	let intersectY = start.y + gradient * (start.x - Math.floor(start.x) + 0.5)

	const newPoints: Point[] = []
	for (let x = Math.floor(start.x); x <= Math.floor(end.x); x++) {
		let opacity
		if (steep) {
			opacity = 1 - (intersectY - Math.floor(intersectY))
			newPoints.push({ x: Math.floor(intersectY), y: x, opacity, color })
			newPoints.push({
				x: Math.floor(intersectY) + 1,
				y: x,
				opacity: 1 - opacity,
				color,
			})
		} else {
			opacity = 1 - (intersectY - Math.floor(intersectY))
			newPoints.push({ x, y: Math.floor(intersectY), opacity, color })
			newPoints.push({
				x,
				y: Math.floor(intersectY) + 1,
				opacity: 1 - opacity,
				color,
			})
		}
		intersectY += gradient
	}
	return newPoints
}
