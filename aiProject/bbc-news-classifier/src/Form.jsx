import React, { useState } from 'react';
import './Form.css';

const Form = () => {
  const [text, setText] = useState('');
  const [category, setCategory] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    try {
      const response = await fetch('http://127.0.0.1:5000/api/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text }),
      });
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      setCategory(data.category);
    } catch (err) {
      setError('Failed to fetch the category. Please try again.');
    }
  };

  return (
    <div className="form-container">
      <h1>BBC News Topic Classification</h1>
      <form className='form' onSubmit={handleSubmit}>
        <textarea required
          className="text-area"
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Enter News here..."
        />
        <button className="submit-button" type="submit">Predict</button>
      </form>
      {category && (
        <div className="category-container">
          <p className="category-text">Predicted Category:<p className="category">{category}</p></p>
          
        </div>
      )}
      {error && <p className="error-message">{error}</p>}
    </div>
  );
};

export default Form;
