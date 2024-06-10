from pyspark.sql.functions import col, when, count
import logging

logger = logging.getLogger("functions")

class cleaningFunctions():
    
    def count_nulls(df, columns_to_check):
        """
        Count null values in specified columns of a DataFrame.
        
        Args:
            df (DataFrame): Spark DataFrame.
            columns_to_check (list): List of column names to check for nulls.
        
        Returns:
            DataFrame: DataFrame containing counts of null values in specified columns.
        """
        try:
            null_counts = df.select([count(when(col(c).isNull(), c)).alias(c) for c in columns_to_check])
            return null_counts
        
        except Exception as e:
            logger.info("An error occurred:" + str(e))
            return None
