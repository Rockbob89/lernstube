"""
Task 2: PySpark on Databricks — Solutions

These stubs assume a SparkSession is available (as in a Databricks notebook).
Fill in the transformations.
"""

from pyspark.sql import SparkSession, DataFrame, Window
from pyspark.sql import functions as F


spark = SparkSession.builder.getOrCreate()


# --- Sample data creation (for local testing) ---
def create_sample_rides() -> DataFrame:
    """Create a sample taxi rides DataFrame for testing."""
    from datetime import datetime
    data = [
        (datetime(2024, 1, 1, 8, 0), datetime(2024, 1, 1, 8, 25), "Zone_A", "Zone_B", 15.0, 3.0, 18.0, 2),
        (datetime(2024, 1, 1, 9, 0), datetime(2024, 1, 1, 9, 10), "Zone_A", "Zone_C", 8.0, 1.5, 9.5, 1),
        (datetime(2024, 1, 1, 10, 0), datetime(2024, 1, 1, 10, 45), "Zone_B", "Zone_A", 22.0, 5.0, 27.0, 3),
    ]
    schema = "pickup_time timestamp, dropoff_time timestamp, pickup_zone string, dropoff_zone string, fare double, tip double, total double, passenger_count int"
    return spark.createDataFrame(data, schema)


def create_sample_zones() -> DataFrame:
    """Create a sample zones DataFrame for testing."""
    data = [
        ("Zone_A", "Manhattan", "Upper East Side"),
        ("Zone_B", "Brooklyn", "Williamsburg"),
        ("Zone_C", "Manhattan", "Midtown"),
    ]
    return spark.createDataFrame(data, "zone_id string, borough string, zone_name string")


# --- Exercise 1: Transformation Pipeline ---
def transformation_pipeline(rides: DataFrame) -> DataFrame:
    """
    Add duration_min, filter 2-120 min, add tip_pct,
    group by pickup_zone with aggregations, sort by total rides desc.
    """
    # TODO: implement
    return rides


# --- Exercise 2: Window Functions ---
def rank_zones_by_hourly_revenue(rides: DataFrame) -> DataFrame:
    """Rank zones by total revenue (fare + tip) per hour."""
    # TODO: implement
    return rides


def rolling_avg_daily_rides(rides: DataFrame) -> DataFrame:
    """7-day rolling average of daily ride count."""
    # TODO: implement
    return rides


def busiest_hour_per_zone(rides: DataFrame) -> DataFrame:
    """Find the busiest hour for each zone."""
    # TODO: implement
    return rides


# --- Exercise 3: Joins ---
def join_with_broadcast(rides: DataFrame, zones: DataFrame) -> DataFrame:
    """Join rides to zones using broadcast (for small zones table)."""
    # TODO: implement
    return rides


def join_without_broadcast(rides: DataFrame, zones: DataFrame) -> DataFrame:
    """Join rides to zones without broadcast hint."""
    # TODO: implement
    return rides


# --- Explanation stub ---
def broadcast_vs_sort_merge() -> str:
    """
    When to use broadcast join vs sort-merge join?
    Return your explanation.
    """
    return ""


if __name__ == "__main__":
    rides = create_sample_rides()
    zones = create_sample_zones()

    print("=== Exercise 1: Transformation Pipeline ===")
    transformation_pipeline(rides).show()

    print("=== Exercise 2a: Hourly Revenue Ranking ===")
    rank_zones_by_hourly_revenue(rides).show()

    print("=== Exercise 2b: Rolling Average ===")
    rolling_avg_daily_rides(rides).show()

    print("=== Exercise 2c: Busiest Hour ===")
    busiest_hour_per_zone(rides).show()

    print("=== Exercise 3: Joins ===")
    join_with_broadcast(rides, zones).show()
    print(broadcast_vs_sort_merge())
