import { useState } from 'react'

import Lab1 from '../Lab1/Lab1'
import Lab2 from '../Lab2/Lab2'
import Lab3 from '../Lab3/Lab3'
import Lab4 from '../Lab4/Lab4'
import Lab5 from '../Lab5/Lab5'
import Lab6 from '../Lab6/Lab6'
import Lab7 from '../Lab7/Lab7'

import './App.css'

function App() {
	const [selectedLab, setSelectedLab] = useState(7)

	const handleLabChange = (labNumber: number) => {
		setSelectedLab(labNumber)
	}

	return (
		<div className='MainWrapper'>
			<div className='Main'>
				<div className='LabSelection'>
					<label>Лабораторная </label>
					<div>
						<button
							className={selectedLab === 1 ? 'selected' : ''}
							onClick={() => handleLabChange(1)}
						>
							1
						</button>
						<button
							className={selectedLab === 2 ? 'selected' : ''}
							onClick={() => handleLabChange(2)}
						>
							2
						</button>
						<button
							className={selectedLab === 3 ? 'selected' : ''}
							onClick={() => handleLabChange(3)}
						>
							3
						</button>
						<button
							className={selectedLab === 4 ? 'selected' : ''}
							onClick={() => handleLabChange(4)}
						>
							4
						</button>
						<button
							className={selectedLab === 5 ? 'selected' : ''}
							onClick={() => handleLabChange(5)}
						>
							5
						</button>
						<button
							className={selectedLab === 6 ? 'selected' : ''}
							onClick={() => handleLabChange(6)}
						>
							6
						</button>
						<button
							className={selectedLab === 7 ? 'selected' : ''}
							onClick={() => handleLabChange(7)}
						>
							7
						</button>
					</div>
				</div>
				{selectedLab === 1 && <Lab1 />}
				{selectedLab === 2 && <Lab2 />}
				{selectedLab === 3 && <Lab3 />}
				{selectedLab === 4 && <Lab4 />}
				{selectedLab === 5 && <Lab5 />}
				{selectedLab === 6 && <Lab6 />}
				{selectedLab === 7 && <Lab7 />}
			</div>
		</div>
	)
}

export default App
