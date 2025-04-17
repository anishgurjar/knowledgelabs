import { useState } from 'react';
import './App.css';
import { useEffect } from 'react';
import axios from 'axios';

const Quote = ({ refreshTrigger = 0 }) => {
    const [quote, setQuote] = useState({"q":"", "a": ""});
    const [isLoading, setIsLoading] = useState(false);

    useEffect(() => {
        const getQuote = async () => {
            setIsLoading(true);
            try {
                const response = await axios.post('https://api.openai.com/v1/chat/completions', {
                    model: "gpt-3.5-turbo",
                    messages: [{
                        role: "user",
                        content: "Give me an inspirational quote and its author in the exact format: 'QUOTE - AUTHOR'. Niche tech people"
                    }]
                }, {
                    headers: {
                        'Authorization': `Bearer ${import.meta.env.VITE_OPENAI_API_KEY}`,
                        'Content-Type': 'application/json'
                    }
                });
                const content = response.data.choices[0].message.content;
                const [quoteText, author] = content.split(' - ');
                if (!quoteText || !author) {
                    throw new Error('Invalid quote format');
                }
                setQuote({ q: quoteText.trim(), a: author.trim() });
            } catch (error) {
                console.error('Error fetching quote:', error);
                setQuote({ q: "Error loading quote", a: "System" });
            } finally {
                setIsLoading(false);
            }
        }
        getQuote();
    }, [refreshTrigger])

    return (
        <div className="quote-box">
            {isLoading ? (
                <div className="quote-loader">Loading...</div>
            ) : (
                <>
                    <p className="quote-text">
                        {quote.q}
                    </p>
                    <p className="quote-author">- {quote.a}</p>
                </>
            )}
        </div>
    );
};

export default Quote;
