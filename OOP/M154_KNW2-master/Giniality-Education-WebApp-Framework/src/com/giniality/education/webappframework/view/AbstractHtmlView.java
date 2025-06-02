package com.giniality.education.webappframework.view;

/**
 * This abstract class provides methods to create a titled
 * header and a footer of an HTML page. Additionally this class
 * implements the getter and setter methods for the display object.
 * 
 * Subclasses only have to implement the 
 * <code>createPageContents</code> method.
 * 
 * @author Christian Sauer (CSA), Giniality AG
 */
public abstract class AbstractHtmlView implements View {

	/**
	 * The display <code>Object</code> of the <code>View</code>.
	 */
	private Object displayObject;

	/**
	 * Set the object to use for display.
	 * 
	 * @param inDisplayObject The object.
	 */
	public void setDisplayObject(Object inDisplayObject) {
		displayObject = inDisplayObject;
	}

	/**
	 * Gets the object to be used for display.
	 * 
	 * @return The display object.
	 */
	protected Object getDisplayObject() {
		return displayObject;
	}

	/**
	 * Returns the predefined header of the HTML page and 
	 * sets the given page title.
	 * 
	 * @param inPageTitle The title of the resulting HTML page.
	 * 
	 * @return The HTML page header.
	 */
	protected String createHtmlPageHeader() {
		String outString =
			"<html>\n"
				+ "<head>\n"
				+ "<title>"
				+ getTitle()
				+ "</title>\n"
				+ "<link rel='stylesheet' type='text/css' href='style/styles.css'>"
				+ "</head>\n"
				+ "<body vlink=\"#0000A0\" link=\"#0000A0\">\n<br />\n";

		return outString;
	}

	/**
	 * Returns the predefined footer of the HTML page.
	 * 
	 * @return The HTML page footer.
	 */
	protected String createHtmlPageFooter() {
		String outFooter = "<form action='index.html'><input type='submit' value='zurück zum Menü'>"
							+ "</form></body>\n</html>";

		return outFooter;
	}

	/**
	 * Creates the contents of this current view. 
	 * 
	 * Implement this method in subclasses in order to
	 * define custom page contents depending on the display
	 * object that has been set on the <code>View</code>.
	 * 
	 * @return The contents of this view.
	 */
	protected abstract String createPageContents();
	
	/**
	 * @see com.giniality.education.webappframework.view.View#show()
	 */
	public String show() {
		StringBuffer aPageContentBuffer = new StringBuffer();
		
		aPageContentBuffer.append(createHtmlPageHeader());
		aPageContentBuffer.append(createPageContents());
		aPageContentBuffer.append(createHtmlPageFooter());
		
		return aPageContentBuffer.toString();
	}

}