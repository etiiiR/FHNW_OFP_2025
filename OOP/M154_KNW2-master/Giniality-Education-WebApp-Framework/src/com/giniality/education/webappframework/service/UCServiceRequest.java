package com.giniality.education.webappframework.service;

import java.util.Iterator;
import java.util.Map;

/**
 * This service request transforms a http request
 * into a neutral request object containing the
 * parameters as string values.
 * 
 * @author Christian Sauer (CSA), Giniality AG
 */
final class UCServiceRequest extends AbstractServiceRequest {

	/**
	 * Default constructor initializing mandatory fields.
	 * 
	 *  @param inRequestMap The original request map. 
	 */
	protected UCServiceRequest(Map inRequestMap) {
		super();

		Iterator aParameterNamesList = inRequestMap.keySet().iterator();
		while (aParameterNamesList.hasNext() == true) {

			// get current parameter name
			String aCurrentParamName = (String) aParameterNamesList.next();
			String[] aValue = (String[]) inRequestMap.get(aCurrentParamName);

			if (aValue != null && aValue.length > 0) {

				// put original param value into parameter map
				parameters.put(aCurrentParamName, aValue[0]);
			} // if
		} //while
	}
}
