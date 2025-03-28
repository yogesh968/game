import React, { useState } from "react";
import SlidingPuzzle from "./SlidingPuzzle";

function App() {
  const [gridSize, setGridSize] = useState(3);
  const [imageMode, setImageMode] = useState(false);
  const imageUrl = "https://source.unsplash.com/300x300/?nature";

  return (
    <div className="container">
      <div className="game-wrapper">
  <h1 className="title">Sliding Puzzle Game 🧩</h1>
  {/* <SlidingPuzzle gridSize={gridSize} imageMode={imageMode} /> */}
</div>

      
      <div>
        <label>Grid Size: </label>
        <button><select onChange={(e) => setGridSize(Number(e.target.value))} value={gridSize}>
          <option value="3">3x3</option>
          <option value="4">4x4</option>
          <option value="5">5x5</option>
        </select></button>
        <label> Image Mode: </label>
        <input type="checkbox" onChange={() => setImageMode(!imageMode)} />
      </div>
      <SlidingPuzzle gridSize={gridSize} imageUrl={imageUrl} />
    </div>
  );
}

export default App;

