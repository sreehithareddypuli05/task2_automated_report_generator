#!/usr/bin/env python3
"""
Standalone Automated Report Generator
====================================================
Required Libraries: pandas, matplotlib, seaborn, reportlab, openpyxl, numpy
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
import os
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

class AutomatedReportGenerator:
    """Fixed version of the Automated Report Generator."""
    
    def __init__(self, output_filename="automated_report.pdf"):
        self.output_filename = output_filename
        self.data = None
        self.analysis_results = {}
        self.chart_files = []
        
        plt.style.use('seaborn-v0_8')
        sns.set_palette("husl")
        
        if not os.path.exists('temp_charts'):
            os.makedirs('temp_charts')
    
    def load_data(self, file_path):
        """Load data from CSV or Excel file - FIXED VERSION."""
        try:
            file_extension = os.path.splitext(file_path)[1].lower()
            
            if file_extension == '.csv':
                self.data = pd.read_csv(file_path)
                print(f"✅ Successfully loaded CSV file: {file_path}")
            elif file_extension in ['.xlsx', '.xls']:
                self.data = pd.read_excel(file_path)
                print(f"✅ Successfully loaded Excel file: {file_path}")
            else:
                raise ValueError(f"Unsupported file format: {file_extension}")
            
            print(f"📊 Data Shape: {self.data.shape[0]} rows, {self.data.shape[1]} columns")
            print(f"📋 Columns: {list(self.data.columns)}")
            
            return self.data
            
        except Exception as e:
            print(f"❌ Error loading file: {str(e)}")
            return None
    
    def analyze_data(self):
        """Perform comprehensive data analysis - FIXED VERSION."""
        # FIX: Proper DataFrame checking
        if self.data is None or self.data.empty:
            print("❌ No data loaded. Please load data first.")
            return None
        
        print("🔍 Performing data analysis...")
        
        # Basic info
        self.analysis_results['basic_info'] = {
            'total_rows': len(self.data),
            'total_columns': len(self.data.columns),
            'column_names': list(self.data.columns),
            'data_types': dict(self.data.dtypes.astype(str)),
            'missing_values': dict(self.data.isnull().sum())
        }
        
        # FIX: Convert pandas Index to list and add error handling
        numeric_columns = self.data.select_dtypes(include=[np.number]).columns.tolist()
        if len(numeric_columns) > 0:
            self.analysis_results['numerical_stats'] = {}
            for col in numeric_columns:
                try:
                    self.analysis_results['numerical_stats'][col] = {
                        'mean': float(self.data[col].mean()),
                        'median': float(self.data[col].median()),
                        'std': float(self.data[col].std()),
                        'min': float(self.data[col].min()),
                        'max': float(self.data[col].max()),
                        'q25': float(self.data[col].quantile(0.25)),
                        'q75': float(self.data[col].quantile(0.75))
                    }
                except Exception as e:
                    print(f"⚠️ Warning: Could not analyze column {col}: {e}")
                    continue
        
        # FIX: Convert pandas Index to list and add error handling
        categorical_columns = self.data.select_dtypes(include=['object']).columns.tolist()
        if len(categorical_columns) > 0:
            self.analysis_results['categorical_stats'] = {}
            for col in categorical_columns:
                try:
                    value_counts = self.data[col].value_counts()
                    self.analysis_results['categorical_stats'][col] = {
                        'unique_values': int(self.data[col].nunique()),
                        'most_frequent': str(value_counts.index[0]) if len(value_counts) > 0 else 'N/A',
                        'frequency': int(value_counts.iloc[0]) if len(value_counts) > 0 else 0,
                        'value_counts': dict(value_counts.head(10).to_dict())
                    }
                except Exception as e:
                    print(f"⚠️ Warning: Could not analyze column {col}: {e}")
                    continue
        
        # Data quality assessment
        try:
            total_cells = len(self.data) * len(self.data.columns)
            missing_cells = self.data.isnull().sum().sum()
            completeness_rate = ((total_cells - missing_cells) / total_cells) * 100 if total_cells > 0 else 0
            
            self.analysis_results['data_quality'] = {
                'completeness_rate': float(completeness_rate),
                'duplicate_rows': int(self.data.duplicated().sum()),
                'unique_rows': int(len(self.data) - self.data.duplicated().sum())
            }
        except Exception as e:
            print(f"⚠️ Warning: Could not calculate data quality metrics: {e}")
            self.analysis_results['data_quality'] = {
                'completeness_rate': 0.0,
                'duplicate_rows': 0,
                'unique_rows': len(self.data) if self.data is not None else 0
            }
        
        print("✅ Data analysis completed!")
        return self.analysis_results
    
    def create_visualizations(self):
        """Create and save visualizations - FIXED VERSION."""
        # FIX: Proper DataFrame checking
        if self.data is None or self.data.empty:
            print("❌ No data available for visualization.")
            return []
        
        print("📊 Creating visualizations...")
        
        # FIX: Convert to list
        numeric_columns = self.data.select_dtypes(include=[np.number]).columns.tolist()
        categorical_columns = self.data.select_dtypes(include=['object']).columns.tolist()
        
        chart_count = 0
        
        # 1. Numerical distributions
        if len(numeric_columns) > 0:
            try:
                fig, axes = plt.subplots(2, 2, figsize=(15, 10))
                fig.suptitle('Numerical Data Distributions', fontsize=16, fontweight='bold')
                axes = axes.flatten()
                
                for i, col in enumerate(numeric_columns[:4]):
                    if i < len(axes):
                        self.data[col].hist(bins=20, ax=axes[i], color='skyblue', alpha=0.7, edgecolor='black')
                        axes[i].set_title(f'{col} Distribution', fontweight='bold')
                        axes[i].set_xlabel(col)
                        axes[i].set_ylabel('Frequency')
                        axes[i].grid(True, alpha=0.3)
                
                for i in range(len(numeric_columns), len(axes)):
                    axes[i].set_visible(False)
                
                plt.tight_layout()
                chart_filename = f'temp_charts/numerical_distributions_{chart_count}.png'
                plt.savefig(chart_filename, dpi=300, bbox_inches='tight')
                plt.close()
                self.chart_files.append(chart_filename)
                chart_count += 1
                
            except Exception as e:
                print(f"⚠️ Warning: Could not create numerical distributions: {e}")
        
        # 2. Categorical analysis
        if len(categorical_columns) > 0:
            try:
                fig, axes = plt.subplots(2, 2, figsize=(15, 10))
                fig.suptitle('Categorical Data Analysis', fontsize=16, fontweight='bold')
                axes = axes.flatten()
                
                for i, col in enumerate(categorical_columns[:4]):
                    if i < len(axes) and self.data[col].nunique() <= 20:
                        value_counts = self.data[col].value_counts().head(10)
                        colors_list = plt.cm.Blues(np.linspace(0.3, 0.9, len(value_counts)))
                        bars = axes[i].bar(range(len(value_counts)), value_counts.values, 
                                         color=colors_list, alpha=0.7, edgecolor='black')
                        axes[i].set_title(f'{col} Distribution', fontweight='bold')
                        axes[i].set_xlabel(col)
                        axes[i].set_ylabel('Count')
                        axes[i].set_xticks(range(len(value_counts)))
                        axes[i].set_xticklabels(value_counts.index, rotation=45, ha='right')
                        axes[i].grid(True, alpha=0.3)
                
                for i in range(min(len(categorical_columns), 4), len(axes)):
                    axes[i].set_visible(False)
                
                plt.tight_layout()
                chart_filename = f'temp_charts/categorical_analysis_{chart_count}.png'
                plt.savefig(chart_filename, dpi=300, bbox_inches='tight')
                plt.close()
                self.chart_files.append(chart_filename)
                chart_count += 1
                
            except Exception as e:
                print(f"⚠️ Warning: Could not create categorical analysis: {e}")
        
        # 3. Correlation heatmap
        if len(numeric_columns) >= 2:
            try:
                plt.figure(figsize=(12, 8))
                correlation_matrix = self.data[numeric_columns].corr()
                
                mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
                sns.heatmap(correlation_matrix, mask=mask, annot=True, cmap='coolwarm', 
                           center=0, square=True, cbar_kws={'label': 'Correlation Coefficient'})
                plt.title('Correlation Matrix of Numerical Variables', fontsize=16, fontweight='bold', pad=20)
                plt.tight_layout()
                
                chart_filename = f'temp_charts/correlation_heatmap_{chart_count}.png'
                plt.savefig(chart_filename, dpi=300, bbox_inches='tight')
                plt.close()
                self.chart_files.append(chart_filename)
                chart_count += 1
                
            except Exception as e:
                print(f"⚠️ Warning: Could not create correlation heatmap: {e}")
        
        print(f"✅ Created {len(self.chart_files)} visualizations")
        return self.chart_files
    
    def generate_pdf_report(self, title="Automated Data Analysis Report", author="Report Generator"):
        """Generate PDF report - FIXED VERSION."""
        # FIX: Proper DataFrame and results checking
        if self.data is None or self.data.empty or not self.analysis_results:
            print("❌ No data or analysis results available.")
            return None
        
        print("📄 Generating PDF report...")
        
        try:
            doc = SimpleDocTemplate(self.output_filename, pagesize=A4, 
                                  rightMargin=72, leftMargin=72, 
                                  topMargin=72, bottomMargin=18)
            
            styles = getSampleStyleSheet()
            story = []
            
            # Title
            title_style = ParagraphStyle(
                'CustomTitle',
                parent=styles['Heading1'],
                fontSize=24,
                spaceAfter=30,
                alignment=TA_CENTER,
                textColor=colors.darkblue
            )
            
            story.append(Paragraph(title, title_style))
            story.append(Spacer(1, 20))
            
            # Metadata table
            metadata_data = [
                ['Report Generated:', datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
                ['Author:', author],
                ['Total Records:', str(self.analysis_results['basic_info']['total_rows'])],
                ['Total Columns:', str(self.analysis_results['basic_info']['total_columns'])]
            ]
            
            metadata_table = Table(metadata_data, colWidths=[2*inch, 3*inch])
            metadata_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, -1), colors.lightgrey),
                ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 12),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            
            story.append(metadata_table)
            story.append(PageBreak())
            
            # Data Summary
            heading_style = ParagraphStyle(
                'CustomHeading',
                parent=styles['Heading2'],
                fontSize=16,
                spaceAfter=12,
                spaceBefore=20,
                textColor=colors.darkblue
            )
            
            story.append(Paragraph("Data Summary", heading_style))
            
            # Basic stats table
            if 'numerical_stats' in self.analysis_results and self.analysis_results['numerical_stats']:
                summary_data = [['Column', 'Mean', 'Median', 'Std Dev', 'Min', 'Max']]
                
                for col, stats in self.analysis_results['numerical_stats'].items():
                    summary_data.append([
                        col,
                        f"{stats['mean']:.2f}",
                        f"{stats['median']:.2f}", 
                        f"{stats['std']:.2f}",
                        f"{stats['min']:.2f}",
                        f"{stats['max']:.2f}"
                    ])
                
                summary_table = Table(summary_data, colWidths=[1.2*inch, 0.8*inch, 0.8*inch, 0.8*inch, 0.8*inch, 0.8*inch])
                summary_table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 0), (-1, 0), 11),
                    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                    ('FONTSIZE', (0, 1), (-1, -1), 10),
                    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.beige, colors.white]),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black)
                ]))
                
                story.append(summary_table)
            
            # Add visualizations
            if self.chart_files:
                story.append(PageBreak())
                story.append(Paragraph("Data Visualizations", heading_style))
                
                for chart_file in self.chart_files:
                    if os.path.exists(chart_file):
                        img = Image(chart_file, width=6*inch, height=4*inch)
                        story.append(img)
                        story.append(Spacer(1, 20))
            
            # Build PDF
            doc.build(story)
            
            print(f"✅ PDF report generated successfully: {self.output_filename}")
            
            # Cleanup
            self._cleanup_temp_files()
            
            return self.output_filename
            
        except Exception as e:
            print(f"❌ Error generating PDF: {e}")
            return None
    
    def _cleanup_temp_files(self):
        """Clean up temporary files."""
        for chart_file in self.chart_files:
            try:
                if os.path.exists(chart_file):
                    os.remove(chart_file)
            except Exception:
                pass
        
        try:
            if os.path.exists('temp_charts') and not os.listdir('temp_charts'):
                os.rmdir('temp_charts')
        except Exception:
            pass
    
    def run_complete_analysis(self, file_path, report_title="Data Analysis Report", author="Analyst"):
        """Run complete analysis pipeline - FIXED VERSION."""
        print("🚀 Starting Analysis Pipeline...")
        print("=" * 40)
        
        # Load data
        loaded_data = self.load_data(file_path)
        if loaded_data is None:
            print("❌ Failed to load data. Aborting analysis.")
            return None
        
        # Analyze
        analysis_result = self.analyze_data()
        if analysis_result is None:
            print("❌ Failed to analyze data. Aborting report generation.")
            return None
        
        # Visualize
        self.create_visualizations()
        
        # Generate report
        report_path = self.generate_pdf_report(title=report_title, author=author)
        
        if report_path:
            print("\n🎉 SUCCESS!")
            print(f"📄 Report: {report_path}")
            print(f"📊 Records: {len(self.data)}")
            print(f"📈 Charts: {len(self.chart_files)}")
        
        return report_path

def main():
    """Main function - FIXED VERSION."""
    print("📊 AUTOMATED REPORT GENERATOR (FIXED VERSION)")
    print("=" * 50)
    
    # Get file path
    file_path = input("Enter path to your CSV/Excel file: ").strip()
    
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return
    
    # Get report details
    title = input("Enter report title (or press Enter for default): ").strip()
    if not title:
        title = "Data Analysis Report"
    
    author = input("Enter author name (or press Enter for default): ").strip()
    if not author:
        author = "Data Analyst"
    
    # Generate report
    generator = AutomatedReportGenerator("analysis_report.pdf")
    generator.run_complete_analysis(file_path, title, author)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 Interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()