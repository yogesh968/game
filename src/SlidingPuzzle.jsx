import React, { useState, useEffect } from "react";
import "./SlidingPuzzle.css";

const SlidingPuzzle = ({ gridSize = 3, imageMode = false, imageUrl = "" }) => {
  const generateBoard = () => {
    let numbers = Array.from({ length: gridSize * gridSize }, (_, i) => i);
    numbers.sort(() => Math.random() - 0.5);
    return numbers;
  };

  const [tiles, setTiles] = useState(generateBoard());
  const [moves, setMoves] = useState(0);
  const [time, setTime] = useState(0);
  const [gameWon, setGameWon] = useState(false);
  const emptyIndex = tiles.indexOf(0);

  useEffect(() => {
    if (!gameWon) {
      const timer = setInterval(() => setTime((prev) => prev + 1), 1000);
      return () => clearInterval(timer);
    }
  }, [gameWon]);

  useEffect(() => {
    if (gameWon) {
      saveHighScore(moves, time);
    }
  }, [gameWon]);

  const handleMove = (index) => {
    if (gameWon) return;
    const row = Math.floor(index / gridSize);
    const col = index % gridSize;
    const emptyRow = Math.floor(emptyIndex / gridSize);
    const emptyCol = emptyIndex % gridSize;

    if (
      (Math.abs(row - emptyRow) === 1 && col === emptyCol) ||
      (Math.abs(col - emptyCol) === 1 && row === emptyRow)
    ) {
      let newTiles = [...tiles];
      [newTiles[index], newTiles[emptyIndex]] = [newTiles[emptyIndex], newTiles[index]];
      setTiles(newTiles);
      setMoves(moves + 1);
      if (checkWin(newTiles)) {
        setGameWon(true);
      }
    }
  };

  const checkWin = (tilesArray) => {
    return tilesArray.every((tile, index) => tile === index);
  };

  const resetGame = () => {
    setTiles(generateBoard());
    setMoves(0);
    setTime(0);
    setGameWon(false);
  };

  const saveHighScore = (moves, time) => {
    let scores = JSON.parse(localStorage.getItem("puzzleScores")) || [];
    scores.push({ moves, time });
    scores.sort((a, b) => a.time - b.time || a.moves - b.moves);
    scores = scores.slice(0, 3); // Keep only top 3 scores
    localStorage.setItem("puzzleScores", JSON.stringify(scores));
  };

  return (
    <div>
      <h2>Moves: {moves}</h2>
      <h2>Time: {time} sec</h2>
      <div className="puzzle-container" style={{ gridTemplateColumns: `repeat(${gridSize}, 100px)` }}>
        {tiles.map((tile, index) => (
          <div
            key={index}
            className={`tile ${tile === 0 ? "empty" : ""}`}
            onClick={() => handleMove(index)}
            style={
              imageMode && tile !== 0
                ? {
                    backgroundImage: `url(${imageUrl})`,
                    backgroundSize: `${gridSize * 100}px ${gridSize * 100}px`,
                    backgroundPosition: `${(tile % gridSize) * -100}px ${Math.floor(tile / gridSize) * -100}px`,
                  }
                : {}
            }
          >
            {!imageMode && tile !== 0 ? tile : ""}
          </div>
        ))}
      </div>
      {gameWon && <p className="win-message">🎉 You won! 🎉</p>}
      <button className="reset-button" onClick={resetGame}>Restart</button>
      <Leaderboard />
    </div>
  );
};

const Leaderboard = () => {
  const scores = JSON.parse(localStorage.getItem("puzzleScores")) || [];

  return (
    <div className="leaderboard">
      <h3>🏆 Leaderboard 🏆</h3>
      {scores.length === 0 ? <p>No scores yet!</p> : 
        <ul>
          {scores.map((score, index) => (
            <li key={index}>
              <strong>#{index + 1}</strong> - ⏱ {score.time} sec | 🎯 {score.moves} moves
            </li>
          ))}
        </ul>
      }
    </div>
  );
};

export default SlidingPuzzle;
