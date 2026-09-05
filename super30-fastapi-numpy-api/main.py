import logging
from typing import Any

from fastapi import FastAPI
import numpy as np

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI(
    title="NumPy Calculation API",
    version="1.0.0",
    description="Numerical Analysis API using FastAPI GET endpoints and NumPy",
)

# Base NumPy array for statistical analysis
data = np.array([12, 15, 23, 42, 56, 78, 89, 90, 34, 67, 18, 99])


@app.get("/numbers")
def get_numbers() -> dict[str, list[int]]:
    logger.info("Fetching raw numbers array")
    return {"numbers": data.tolist()}


@app.get("/mean")
def get_mean() -> dict[str, float]:
    result = float(np.mean(data))
    return {"mean": result}


@app.get("/median")
def get_median() -> dict[str, float]:
    result = float(np.median(data))
    return {"median": result}


@app.get("/std")
def get_std() -> dict[str, float]:
    result = float(np.std(data))
    return {"standard_deviation": result}


@app.get("/variance")
def get_variance() -> dict[str, float]:
    result = float(np.var(data))
    return {"variance": result}


@app.get("/maximum")
def get_maximum() -> dict[str, int]:
    result = int(np.max(data))
    return {"maximum": result}


@app.get("/minimum")
def get_minimum() -> dict[str, int]:
    result = int(np.min(data))
    return {"minimum": result}


@app.get("/sum")
def get_sum() -> dict[str, int]:
    result = int(np.sum(data))
    return {"sum": result}


@app.get("/even")
def get_even() -> dict[str, list[int]]:
    even_mask = data % 2 == 0
    even_numbers = data[even_mask]
    return {"even_numbers": even_numbers.tolist()}


@app.get("/odd")
def get_odd() -> dict[str, list[int]]:
    odd_mask = data % 2 != 0
    odd_numbers = data[odd_mask]
    return {"odd_numbers": odd_numbers.tolist()}


@app.get("/stats")
def get_stats() -> dict[str, float]:
    return {
        "mean": float(np.mean(data)),
        "median": float(np.median(data)),
        "standard_deviation": float(np.std(data)),
        "variance": float(np.var(data)),
        "maximum": float(np.max(data)),
        "minimum": float(np.min(data)),
    }


@app.get("/table/{number}")
def get_multiplication_table(number: int) -> dict[str, Any]:
    # Vectorized multiplication using np.arange
    multipliers = np.arange(1, 11)
    results = multipliers * number

    table = [
        f"{number} x {m} = {r}"
        for m, r in zip(multipliers.tolist(), results.tolist())
    ]

    return {
        "number": number,
        "table": table,
        "multipliers": multipliers.tolist(),
        "results": results.tolist(),
    }