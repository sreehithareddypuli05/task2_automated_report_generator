# 📊 Automated Report Generator - CSV/Excel to PDF Analytics

A powerful Python script that transforms raw data files (CSV/Excel) into comprehensive, professional PDF reports with statistical analysis, visualizations, and actionable insights.

## 🌟 Key Features

- **📁 Multi-format Support**: Works with CSV and Excel files (.xlsx, .xls)
- **📊 Comprehensive Analysis**: Descriptive statistics, distributions, correlations
- **📈 Rich Visualizations**: Histograms, bar charts, correlation heatmaps, box plots
- **📄 Professional PDF Reports**: Well-formatted reports with tables, charts, and insights
- **🎯 Smart Insights**: Automated generation of key findings and recommendations
- **🔧 Easy to Use**: Simple command-line interface with demo data options

## 📋 Prerequisites

### Required Libraries

Install all dependencies with:

```bash
pip install pandas matplotlib seaborn reportlab openpyxl numpy
```

### Individual Package Details:
- **pandas**: Data manipulation and analysis
- **matplotlib**: Data visualization and plotting
- **seaborn**: Statistical data visualization
- **reportlab**: PDF generation and formatting
- **openpyxl**: Excel file reading support
- **numpy**: Numerical computing

## 🚀 Quick Start

### Method 1: Analyze Your Own Data
```bash
python report_generator.py
# Choose option 1 and provide your CSV/Excel file path
```

### Method 2: Demo with Sample Data
```bash
python report_generator.py
# Choose option 2 (Student data) or 3 (Sales data)
```

### Method 3: Direct Script Usage
```python
from report_generator import AutomatedReportGenerator

# Initialize generator
generator = AutomatedReportGenerator("my_report.pdf")

# Option A: Use your own data
generator.run_complete_analysis(
    file_path="your_data.csv",
    report_title="My Data Analysis",
    author="Your Name"
)

# Option B: Use sample data
generator.run_complete_analysis(
    sample_data_type="student_marks",
    report_title="Demo Analysis",
    author="Demo User"
)
```

## 📊 Input Data Formats

### Supported File Types
- **CSV files** (`.csv`)
- **Excel files** (`.xlsx`, `.xls`)

### Data Requirements
- **Headers**: First row should contain column names
- **Mixed Data Types**: Supports numerical and categorical data
- **Missing Values**: Handles missing/null values automatically
- **Size**: Optimized for datasets up to 10,000 rows (can handle larger with modifications)

### Sample Data Formats

#### Student Marks Example (`student_marks.csv`):
```csv
Student_ID,Mathematics_Marks,Physics_Marks,Chemistry_Marks,English_Marks,Biology_Marks,Total_Marks,Average_Marks,Grade,Pass_Status,Age,Gender,City
Student_001,85.2,78.5,92.1,88.0,79.3,423.1,84.6,A,Pass,20,Male,Delhi
Student_002,76.8,82.3,85.5,90.2,88.1,422.9,84.6,A,Pass,19,Female,Mumbai
```

#### Sales Data Example (`sales_data.csv`):
```csv
Sale_ID,Region,Product,Month,Sales_Amount,Quantity,Unit_Price,Salesperson,Customer_Type
S0001,North,Product_A,Jan,5420.50,15,361.37,Sales_01,Existing
S0002,South,Product_B,Feb,7830.25,22,355.92,Sales_05,New
```

## 📈 Analysis Components

### 1. **Data Overview**
- Dataset dimensions (rows × columns)
- Data types identification
- Missing values analysis
- Data quality assessment
- Duplicate records detection

### 2. **Numerical Analysis**
For each numerical column:
- **Descriptive Statistics**: Mean, Median, Standard Deviation
- **Distribution Metrics**: Min, Max, Quartiles
- **Variability Analysis**: Coefficient of Variation
- **Outlier Detection**: IQR-based identification

### 3. **Categorical Analysis**
For each categorical column:
- **Unique Values Count**
- **Most Frequent Categories**
- **Distribution Analysis**
- **Value Frequency Tables**

### 4. **Data Quality Assessment**
- **Completeness Rate**: Percentage of non-missing values
- **Data Consistency**: Duplicate record identification
- **Variable Types**: Automatic classification

### 5. **Correlation Analysis**
- **Correlation Matrix**: Relationships between numerical variables
- **Heatmap Visualization**: Color-coded correlation display

## 📊 Visualization Types

### 1. **Distribution Analysis**
- **Histograms**: Show data distribution patterns
- **Box Plots**: Identify outliers and quartile ranges

### 2. **Categorical Analysis**
- **Bar Charts**: Display category frequencies
- **Value Distribution**: Top categories with percentages

### 3. **Relationship Analysis**
- **Correlation Heatmap**: Variable relationships
- **Statistical Summary**: Comparative analysis

### 4. **Summary Visualizations**
- **Multi-variable Comparison**: Side-by-side analysis
- **Statistical Overview**: Key metrics visualization

## 📄 PDF Report Structure

### 1. **Title Page**
- Report title and metadata
- Generation timestamp
- Author information
- Dataset overview

### 2. **Executive Summary**
- Key findings overview
- Data quality assessment
- High-level insights

### 3. **Data Overview Section**
- Dataset information table
- Column details and types
- Missing values summary

### 4. **Statistical Analysis**
- Numerical variables analysis
- Categorical variables analysis
- Detailed statistics tables

### 5. **Visualizations**
- Distribution charts
- Correlation analysis
- Summary plots

### 6. **Insights & Recommendations**
- Automated key findings
- Data quality observations
- Actionable recommendations

## 🔧 Customization Options

### Report Customization
```python
generator = AutomatedReportGenerator("custom_report.pdf")

# Custom analysis
generator.run_complete_analysis(
    file_path="data.csv",
    report_title="Custom Analysis Report",
    author="Your Organization"
)
```

### Analysis Parameters
```python
# Modify numerical analysis
generator.analyze_data()

# Custom visualizations
generator.create_visualizations()

# Generate with custom settings
generator.generate_pdf_report(
    title="Custom Title",
    author="Custom Author"
)
```

## 📁 Output Files

### Generated Files
1. **PDF Report**: Comprehensive analysis report
2. **Temporary Charts**: Visualization images (auto-deleted)
3. **Console Output**: Real-time progress and summary

### Sample Output Structure
```
📁 Project Directory
├── report_generator.py          # Main script
├── sample.csv               # Input data file
├── analysis_report.pdf  # Generated report
    ├── numerical_distributions_0.png
    ├── categorical_analysis_1.png
    └── correlation_heatmap_2.png
```

## 🎯 Use Cases

### Business Applications
- **Sales Performance Analysis**: Revenue trends, product performance
- **Customer Analytics**: Behavior patterns, demographics
- **Financial Reporting**: Budget analysis, expense tracking
- **Marketing Analytics**: Campaign effectiveness, ROI analysis

### Educational Applications
- **Student Performance**: Grade analysis, subject comparisons
- **Research Data**: Survey results, experimental data
- **Academic Reporting**: Course statistics, assessment analysis

### Healthcare Applications
- **Patient Data Analysis**: Treatment outcomes, demographics
- **Clinical Research**: Study results, statistical analysis
- **Health Metrics**: Performance indicators, quality measures

## 🔍 Error Handling

### Common Issues and Solutions

1. **File Not Found**
   ```
   ❌ File not found: data.csv
   💡 Solution: Check file path and ensure file exists
   ```

2. **Unsupported File Format**
   ```
   ❌ Unsupported file format: .txt
   💡 Solution: Convert to CSV or Excel format
   ```

3. **Empty Dataset**
   ```
   ❌ No data available for analysis
   💡 Solution: Ensure file contains data rows
   ```

4. **Memory Issues**
   ```
   ❌ Memory error with large dataset
   💡 Solution: Process data in chunks or reduce dataset size
   ```

## 🚀 Advanced Features

### Custom Data Types
```python
# Handle specific data scenarios
generator.data['date_column'] = pd.to_datetime(generator.data['date_column'])
generator.data['category_column'] = generator.data['category_column'].astype('category')
```

### Extended Analysis
```python
# Add custom analysis
def custom_analysis(self):
    # Your custom analysis code
    pass

# Integrate with existing pipeline
AutomatedReportGenerator.custom_analysis = custom_analysis
```

## 📊 Sample Reports

The script includes two sample datasets for demonstration:

### 1. Student Marks Dataset
- **Records**: 100 students
- **Variables**: 13 columns including marks, demographics
- **Analysis**: Grade distributions, subject performance, demographics

### 2. Sales Data Dataset
- **Records**: 500 sales transactions
- **Variables**: 9 columns including sales, products, regions
- **Analysis**: Regional performance, product analysis, sales trends

## 🤝 Contributing

### Extending Functionality
- Add new visualization types
- Implement additional statistical tests
- Create custom report templates
- Add support for more file formats

### Code Structure
```python
class AutomatedReportGenerator:
    ├── load_data()              # Data input handling
    ├── analyze_data()           # Statistical analysis
    ├── create_visualizations()  # Chart generation
    ├── generate_pdf_report()    # PDF creation
    └── run_complete_analysis()  # Full pipeline
```

## 📚 Dependencies Details

| Library | Version | Purpose |
|---------|---------|---------|
| pandas | ≥1.3.0 | Data manipulation and analysis |
| matplotlib | ≥3.5.0 | Basic plotting and visualization |
| seaborn | ≥0.11.0 | Statistical data visualization |
| reportlab | ≥3.6.0 | PDF generation and formatting |
| openpyxl | ≥3.0.0 | Excel file reading support |
| numpy | ≥1.21.0 | Numerical computing |

## 🔧 Installation Commands

```bash
# Install all dependencies at once
pip install pandas matplotlib seaborn reportlab openpyxl numpy

# Or install from requirements file
pip install -r requirements.txt

# For conda users
conda install pandas matplotlib seaborn numpy
pip install reportlab openpyxl
```

## 🎯 Performance Tips

### For Large Datasets
- **Sample Data**: Analyze a representative sample first
- **Chunk Processing**: Process data in smaller chunks
- **Memory Management**: Use appropriate data types

### Optimization
```python
# Optimize for large datasets
generator.data = generator.data.sample(n=1000)  # Sample for large data
generator.data = generator.data.astype({'category_col': 'category'})  # Optimize memory
```

## 📞 Support and Documentation

- **Error Messages**: Check console output for detailed error information
- **Log Files**: Monitor progress through printed status messages
- **Documentation**: This README covers all major functionality

---

**Note**: This report generator is designed for educational and business analysis purposes. For production use, consider implementing additional data validation, error handling, and security measures.
