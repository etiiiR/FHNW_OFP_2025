package com.giniality.education.webappframework.service;

/**
 * A <code>Service</code> object is capable of processing
 * an incoming request.
 * 
 * @author Christian Sauer (CSA), Giniality AG
 */
public interface Service {

	/**
	 * Processes the incoming request and returns the resulting
	 * object. See implementing class documentation for type of 
	 * return object and cast correspondingly.
	 * 
	 * @param inRequest The request.
	 */
	public Object process(ServiceRequest inRequest);

	/**
	 * Gets the alias name of this <code>Service</code>
	 * which will be used in forming urls.
	 * 
	 * @return The alias name of this service.
	 */
	public String getAliasName();
}