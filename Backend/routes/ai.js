// // const express = require('express');
// // const router = express.Router();
// // const axios = require('axios');

// // // Route to get AI predictions
// // router.post('/predict', async (req, res) => {
// //     try {
// //         const { forecast_hours } = req.body;

// //         // Forward request to Flask API
// //         const response = await axios.post('http://localhost:5000/predict', { forecast_hours });

// //         // Respond with Flask API data
// //         res.status(response.status).json(response.data);
// //     } catch (error) {
// //         console.error('Error in /api/ai/predict:', error.message);
// //         res.status(500).json({ error: 'Failed to fetch predictions from the AI API.' });
// //     }
// // });

// // // Route to get AI metrics
// // router.get('/metrics', async (req, res) => {
// //     try {
// //         // Forward request to Flask API
// //         const response = await axios.get('http://localhost:5000/metrics');

// //         // Respond with Flask API data
// //         res.status(response.status).json(response.data);
// //     } catch (error) {
// //         console.error('Error in /api/ai/metrics:', error.message);
// //         res.status(500).json({ error: 'Failed to fetch metrics from the AI API.' });
// //     }
// // });


// // module.exports = router;


// const express = require('express');
// const router = express.Router();
// const axios = require('axios');
// const fs = require('fs');
// const { parse } = require('json2csv'); // Import json2csv package

// // Route to get AI predictions
// router.post('/predict', async (req, res) => {
//     try {
//         const { forecast_hours } = req.body;

//         // Forward request to Flask API
//         const response = await axios.post('http://localhost:5000/predict', { forecast_hours });

//         // Assuming the response contains prediction data in the format { date, generation }
//         const predictionData = response.data;

//         // Save the prediction data to CSV
//         saveDataToCSV(predictionData);

//         // Respond with the prediction data
//         res.status(response.status).json(response.data);
//     } catch (error) {
//         console.error('Error in /api/ai/predict:', error.message);
//         res.status(500).json({ error: 'Failed to fetch predictions from the AI API.' });
//     }
// });

// // Function to save data to CSV
// const saveDataToCSV = (data) => {
//     const currentDate = new Date().toISOString().split('T')[0]; // Get the current date in 'YYYY-MM-DD' format
//     const filePath = `./ai/data/solar_generation_${currentDate}.csv`;

//     // Prepare data in the format required for CSV (adding header and values)
//     const csvData = data.map(item => ({
//         date: item.date,
//         generation: item.generation,
//         hour: item.hour
//     }));

//     // Convert JSON to CSV format
//     const csv = parse(csvData);

//     // Write the data to the CSV file (append if the file exists)
//     fs.appendFileSync(filePath, csv + '\n', 'utf8');  // Append to the file

//     console.log(`Data saved to ${filePath}`);
// };

// // Route to get AI metrics
// router.get('/metrics', async (req, res) => {
//     try {
//         // Forward request to Flask API
//         const response = await axios.get('http://localhost:5000/metrics');

//         // Respond with Flask API data
//         res.status(response.status).json(response.data);
//     } catch (error) {
//         console.error('Error in /api/ai/metrics:', error.message);
//         res.status(500).json({ error: 'Failed to fetch metrics from the AI API.' });
//     }
// });

// module.exports = router;


const express = require('express');
const router = express.Router();
const axios = require('axios');

// Route to get AI predictions
router.post('/predict', async (req, res) => {
    try {
        const { forecast_hours } = req.body;

        // Forward request to Flask API
        const response = await axios.post('http://localhost:5000/predict', { forecast_hours });

        // Log and return predictions
        console.log('Predictions:', response.data);
        res.status(200).json({
            message: 'Predictions fetched successfully',
            predictions: response.data,
        });
    } catch (error) {
        console.error('Error in /ai/predict:', error.message);
        res.status(500).json({ error: 'Failed to fetch predictions from the AI API.' });
    }
});

// Route to get AI metrics
router.get('/metrics', async (req, res) => {
    try {
        // Forward request to Flask API
        const response = await axios.get('http://localhost:5000/metrics');

        // Log and return metrics
        console.log('Metrics:', response.data);
        res.status(200).json({
            message: 'Metrics fetched successfully',
            metrics: response.data,
        });
    } catch (error) {
        console.error('Error in /ai/metrics:', error.message);
        res.status(500).json({ error: 'Failed to fetch metrics from the AI API.' });
    }
});
module.exports = router;

// router.get('/consumption/current', async (req, res) => {
//     try {
//         // Path to the consumption file
//         const consumptionFilePath = path.join(__dirname, 
//             '../data/consumption_data.csv'
//         );

//         // Check if the file exists
//         if (!fs.existsSync(consumptionFilePath)) {
//             return res.status(404).json({ error: 'Consumption file not found.' });
//         }

//         const currentDate = new Date();
//         const currentDateString = currentDate.toISOString().split('T')[0]; // Format: YYYY-MM-DD
//         const currentHour = currentDate.getHours();

//         let consumptionDataFound = false;
//         let result = null;

//         // Read and parse the CSV file
//         fs.createReadStream(consumptionFilePath)
//             .pipe(csv())
//             .on('data', (row) => {
//                 if (row.date === currentDateString && parseInt(row.hour) === currentHour) {
//                     result = {
//                         date: row.date,
//                         hour: parseInt(row.hour),
//                         consumption: parseFloat(row.consumption),
//                     };
//                     consumptionDataFound = true;
//                 }
//             })
//             .on('end', () => {
//                 if (consumptionDataFound) {
//                     res.status(200).json({
//                         message: 'Consumption data fetched successfully',
//                         data: result,
//                     });
//                 } else {
//                     res.status(200).json({ message: 'No data found for the current time.' });
//                 }
//             })
//             .on('error', (error) => {
//                 console.error('Error reading consumption file:', error.message);
//                 res.status(500).json({ error: 'Failed to read consumption file.' });
//             });
//     } catch (error) {
//         console.error('Error in /ai/consumption/current:', error.message);
//         res.status(500).json({ error: 'Failed to fetch current consumption data.' });
//     }
// });

// Endpoint for fetching consumption data
router.get('/consumption', async (req, res) => {
    try {
        // Forward request to Flask API to fetch the current consumption
        const response = await axios.get('http://localhost:5000/consumption');
        
        // Log and return the response from Flask
        console.log('Consumption data:', response.data);

        // Check if Flask returned consumption data successfully
        if (response.data.message) {
            return res.status(200).json({
                message: response.data.message,
                data: response.data.data,
            });
        } else {
            return res.status(404).json({ error: 'No consumption data found for the current time' });
        }
    } catch (error) {
        console.error('Error in /ai/consumption:', error.message);
        return res.status(500).json({ error: 'Failed to fetch consumption data from the Flask API.' });
    }
});

const passport = require('passport');  // Ensure you have passport and JWT strategy set up correctly
const fs = require('fs');  // For reading the CSV file

router.get(
    "/consumption",
    passport.authenticate("jwt", { session: false }),  // Add JWT authentication middleware
    async (req, res) => {
        try {
            const csvFilePath = './ai/data/consumption_data.csv'; // Path to your consumption file

            if (!fs.existsSync(csvFilePath)) {
                return res.status(404).json({ error: 'Consumption file not found' });
            }

            const currentDate = new Date();
            const formattedDate = currentDate.toLocaleDateString('en-GB').replace(/\//g, '-'); // Convert to DD-MM-YYYY
            const currentHour = currentDate.getHours().toString().padStart(2, '0') + ':00:00'; // Format hour as HH:00:00

            // Read the CSV file
            const data = fs.readFileSync(csvFilePath, 'utf8');
            const rows = data.split('\n').slice(1); // Skip the header row

            let currentConsumption = null;

            for (const row of rows) {
                const [date, time, consumption] = row.split(',').map((val) => val.trim());

                // Match date and hour
                if (date === formattedDate && time === currentHour) {
                    currentConsumption = parseFloat(consumption); // Convert to float
                    break;
                }
            }

            if (currentConsumption !== null) {
                return res.status(200).json({
                    message: 'Current consumption fetched successfully',
                    date: formattedDate,
                    hour: currentHour,
                    consumption: currentConsumption.toFixed(6), // Ensure consistent decimal format
                });
            } else {
                return res.status(404).json({ message: 'No data found for the current time' });
            }
        } catch (error) {
            console.error('Error in /ai/consumption:', error.message);
            return res.status(500).json({ error: 'Failed to fetch current consumption data.' });
        }
    }
);
module.exports = router;