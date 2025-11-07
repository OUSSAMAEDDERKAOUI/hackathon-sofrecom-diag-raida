// src/components/DataFetcher.tsx

import React, { useEffect } from 'react';

// Define the expected props
interface ApiResponse {
    response: string; 
    model?: string;   
}

interface DataFetcherProps {
    setApiData: React.Dispatch<React.SetStateAction<ApiResponse | null>>;
    setIsLoading: React.Dispatch<React.SetStateAction<boolean>>;
    setError: React.Dispatch<React.SetStateAction<string | null>>;
}

// DataFetcher now accepts props
const DataFetcher: React.FC<DataFetcherProps> = ({ setApiData, setIsLoading, setError }) => {

    const callFlaskEndpoint = async () => {
        const url = 'http://127.0.0.1:5000/api/analysis/';
        
        try {
            // Set initial state via props
            setError(null);
            setIsLoading(true); 

            const response = await fetch(url, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    'what is the answer of x+5=5?': `x=5+5\nx=10`,
                    'what is the answer of 3(x-10)=5?': `3x-10=5\n3x=5+10\n3x=15\nx=15/5\nx=3`,
                    'what is the answer of x+10=4?': `x=4-10\nx=-6`,
                })
            });

            if (!response.ok) {
                const errorBody = await response.text();
                throw new Error(`HTTP error! Status: ${response.status}. Details: ${errorBody}`);
            }

            const data: ApiResponse = await response.json(); 
            
            // 1. Update parent state with fetched data
            setApiData(data);
            
        } catch (err) {
            if (err instanceof Error) {
                console.error('Fetch error:', err.message);
                // 2. Update parent state with error
                setError(err.message);
            } else {
                setError("An unknown error occurred during fetch.");
            }
            
        } finally {
            // 3. Update parent loading state
            setIsLoading(false); 
        }
    };

    // Run the API call once when the component mounts
    useEffect(() => {
        console.log('bb')
        callFlaskEndpoint();
    }, []); 

    // The component does not render the result; it only handles the fetch.
    // It can return null or a small indicator.
    return (
        <div style={{ display: 'none' }}>
            {/* This component is active but renders nothing visible */}
        </div>
    );
};

export default DataFetcher;