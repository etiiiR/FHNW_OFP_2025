package com.giniality.education.webappframework.view;

/**
 * An implementation of this class can display a
 * given display object e.g.:
 * <ul>
 *   <li>Business object</li>
 *   <li>Iterator or List of business objects</li>
 *   <li>etc.</li>
 * </ul>
 * 
 * @author Christian Sauer (CSA), Giniality AG
 */
public interface View {

	/**
	 * Set the object to use for display.
	 * 
	 * @param inDisplayObject The object.
	 */
	public void setDisplayObject(Object inDisplayObject);

	/**
	 * Gets the resulting view in a String representation.
	 * 
	 * @return The String representation of this view.
	 */
	public String show();
	
	/**
	 * Gets the title of this page.
	 * 
	 * @return The title of this page.
	 */
	public String getTitle();
	
	/**
	 * Gets the alias name of this page which will be
	 * used in forming urls.
	 * 
	 * @return The alias name of this page.
	 */
	public String getAliasName();
}