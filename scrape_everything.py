import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

def sanitize_filename(filename):
	invalid_chars = ['<','>',':','"','/','\\','|','?','*']
	for char in invalid_chars:
		filename = filename.replace(char,'')
	return filename

def scrape_urls(url_list):
	results = []
	for url in url_list:
		try:
			response = requests.get(url)
			contents = response.text
			results.append((url, contents))
			st.write(f"Processed: {url}")
		except Exception as e:
			st.write(f"Error processing {url}: {e}")
	return results

def main():
	st.title("Scraping the data from the url's")
	try:
		input_file_name = 'furniture stores pages.csv'
		df = pd.read_csv(input_file_name,header=None)
		urls = df[0].tolist()

		if st.button("Start Scraping"):
			st.write("Processing...")
			scraped_data = scrape_urls(urls)

			output_df = pd.DataFrame(scraped_data, columns=['url', 'contents'])
			output_df.to_csv('output.csv', index=False)

			st.write("Done!")
		"for the first item in the list:"
		if st.button("Generate Formatted data files"):
			outputF = pd.read_csv("output.csv")
			just_text_data = []
			no_attributes_data = []
			for index, row in outputF.iterrows():
				contents = str(row['contents']) if len(str(row['contents']))>0 else ' '
				soup = BeautifulSoup(contents)
				html_soup = BeautifulSoup(contents,'html.parser')

				# Remove everything inside <script> and <style> tags
				for script in html_soup(['script', 'style']):
					script.extract()
				for tag in html_soup.find_all(True):
					for attribute in list(tag.attrs.keys()):
						tag.attrs.pop(attribute)
				cleaned_html = str(html_soup)
				cleaned_html = re.sub(r'\s+', ' ', cleaned_html).strip()
				item_new_contents = re.sub(r'\n', '',re.sub(r'\|+', '|', re.sub(r'\s{2,}', '|',re.sub(r'\t', '|',re.sub("\n","",soup.get_text())))))
				item_new_url = row['url']
				just_text_data.append({"url": item_new_url, "contents": item_new_contents})
				no_attributes_data.append({"url": item_new_url, "contents": cleaned_html})
				index 
				item_new_url
		if st.button('Generate individual files (for labeling)'):
			output_df = pd.read_csv('output_just_text.csv')
			for _ , row in output_df.head(10).iterrows():
				sanitized_name = sanitize_filename(row['url'])
				with open(f"content/{sanitized_name}.txt","w", encoding="utf-8") as f:
					f.write(row['contents'])
				st.write(f"File 'content/{sanitized_name}.txt' created.")
			new_df = pd.DataFrame(just_text_data)
			new_df.to_csv('output_just_text.csv', index=False)
			new_df = pd.DataFrame(no_attributes_data)
			new_df.to_csv('output_no_attributes_html.csv', index=False)
	except FileNotFoundError:
		st.error(input_file_name+" file not found in the current directory.")

if __name__ == "__main__":
	main()

